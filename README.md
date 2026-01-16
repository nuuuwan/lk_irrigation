# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_14:46:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,206 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 14:46:25 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:17:11 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-01-16 14:10:39 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.046 |  |
| 2026-01-16 14:09:06 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:08:18 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:07:26 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:06:49 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.259 |  |
| 2026-01-16 14:06:41 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:06:33 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-01-16 14:06:02 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-01-16 14:05:44 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-16 14:05:12 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:05:07 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-16 14:04:31 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:04:25 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:04:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:03:50 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 14:03:44 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 14:03:40 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-01-16 14:03:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:03:21 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-01-16 14:03:15 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-01-16 14:03:09 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 14:02:58 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-16 14:02:53 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:02:53 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-16 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-01-16 14:02:10 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:02:08 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:01:55 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:01:48 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:01:43 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-16 14:01:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.005 |  |
| 2026-01-16 14:01:23 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:01:21 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-16 14:01:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-16 14:00:54 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-01-16 14:00:41 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:00:21 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.020 |  |
| 2026-01-16 13:59:39 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 14:01:43 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-16 14:02:58 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-16 14:01:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-16 14:03:09 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 14:03:44 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 14:03:50 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 14:02:08 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:04:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:01:23 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:00:41 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:46:25 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:01:48 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:01:55 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:02:53 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:04:31 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:06:41 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:07:26 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:03:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:02:10 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:09:06 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:00:54 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:04:25 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:08:18 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:01:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.005 |  |
| 2026-01-16 14:06:33 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-01-16 14:05:44 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-16 14:02:53 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-16 14:01:21 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-16 14:05:07 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-16 14:03:21 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-01-16 14:17:11 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-01-16 14:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-01-16 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-01-16 14:00:21 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.020 |  |
| 2026-01-16 14:06:02 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.021 |  |
| 2026-01-16 14:03:15 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-01-16 14:03:40 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-01-16 14:10:39 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.046 |  |
| 2026-01-16 14:06:49 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.259 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)