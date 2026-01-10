# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_16:06:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 16:06:19 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-10 16:06:11 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:05:46 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:05:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:04:38 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-10 16:04:32 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:04:17 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-01-10 16:04:16 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:04:04 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-10 16:03:52 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-10 16:03:40 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:03:40 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:03:38 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:03:16 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:03:12 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:51 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:26 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:16 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:16 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-10 16:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:02:03 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-10 16:01:48 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:01:41 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:01:30 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-01-10 16:01:25 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 16:01:24 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:01:17 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.053 |  |
| 2026-01-10 16:01:16 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.020 |  |
| 2026-01-10 16:01:08 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:00:57 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:00:41 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 16:00:23 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:13:08 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-10 15:11:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-10 15:11:14 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:09:11 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 16:04:17 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-01-10 16:04:38 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-10 16:06:19 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-10 16:02:03 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-10 16:04:04 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-10 16:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-10 16:03:52 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-10 16:00:41 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 16:01:25 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 16:01:24 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:26 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:03:40 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:03:16 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:09:11 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:36 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:16 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:03:12 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:03:38 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:06:11 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:05:49 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:04:32 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 15:02:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:01:41 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:16 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:05:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:05:46 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:00:23 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:02:51 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:17:14 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:01:08 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:03:40 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:00:57 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:01:48 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:04:16 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-10 16:01:16 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.020 |  |
| 2026-01-10 16:01:30 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2026-01-10 15:01:58 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.035 |  |
| 2026-01-10 16:01:17 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)