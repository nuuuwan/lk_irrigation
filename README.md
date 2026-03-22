# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_04:11:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,852 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 04:11:43 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:11:02 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:09:11 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:07:39 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-23 04:07:06 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:06:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-23 04:05:56 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-23 04:05:32 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:05:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:04:52 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:04:13 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 04:04:07 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:03:31 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-23 04:03:02 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:02:53 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-03-23 04:02:32 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:02:25 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-03-23 04:02:21 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-23 04:02:18 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:02:08 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-23 04:01:57 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:56 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-23 04:01:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:45 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:44 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:38 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.033 |  |
| 2026-03-23 04:01:28 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.178 |  |
| 2026-03-23 04:01:19 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:16 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:00:43 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-03-23 04:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 03:48:47 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 03:40:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-23 03:37:35 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 04:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-03-23 03:20:23 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-03-23 04:00:43 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-03-23 04:02:08 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-23 04:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 04:04:13 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 04:06:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-23 04:11:02 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:19 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:44 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:11:43 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:00:06 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:05:32 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:07:06 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:09:11 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-23 03:03:17 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:04:07 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:16 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:45 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:03:02 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 03:01:50 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:04:52 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:01:37 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 01:21:26 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:05:56 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:01:57 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:02:18 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-23 04:03:31 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-23 03:02:37 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-23 04:02:21 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-23 04:01:56 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-23 04:07:39 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-23 04:02:53 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-03-23 04:01:38 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.033 |  |
| 2026-03-23 04:02:25 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-03-22 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.051 |  |
| 2026-03-23 04:01:28 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.178 |  |
| 2026-03-23 03:03:29 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -2.795 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)