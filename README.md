# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_05:35:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 05:35:36 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:33:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.102 |  |
| 2026-03-23 05:20:50 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:14:58 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:09:54 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.035 |  |
| 2026-03-23 05:07:54 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:06:34 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-03-23 05:06:31 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:06:25 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:06:19 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-23 05:05:10 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.005 |  |
| 2026-03-23 05:05:00 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-23 05:04:25 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:04:22 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-23 05:04:21 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-23 05:03:53 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.066 |  |
| 2026-03-23 05:03:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:03:26 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:03:25 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:03:23 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:51 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:32 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:21 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:17 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-03-23 05:02:08 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:05 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-23 05:02:02 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-23 05:01:32 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-03-23 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.121 |  |
| 2026-03-23 05:01:01 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-23 05:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 05:00:50 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:00:40 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:00:35 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-23 05:00:19 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:42:32 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.003 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 05:04:21 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-23 04:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-23 05:02:05 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-23 05:04:22 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-23 05:06:19 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-23 05:05:00 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-23 05:01:01 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-23 05:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 05:00:40 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:20:50 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:44 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:21 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:35:36 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:00:06 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:06:25 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:51 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:06:31 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:03:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:32 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:00:50 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:03:26 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:14:58 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:07:54 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:03:25 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:01:37 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:03:23 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-23 05:02:08 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:42:32 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.003 |  |
| 2026-03-23 05:05:10 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.005 |  |
| 2026-03-23 05:02:02 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-23 05:00:35 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-23 05:01:32 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-03-23 05:06:34 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-03-23 05:09:54 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.035 |  |
| 2026-03-23 05:02:17 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-03-22 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.051 |  |
| 2026-03-23 05:03:53 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.066 |  |
| 2026-03-23 05:33:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.102 |  |
| 2026-03-23 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)