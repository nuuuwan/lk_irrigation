# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_23:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 23:03:30 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-05-10 23:03:28 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-10 23:03:17 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-10 23:03:03 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-05-10 23:02:56 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-10 23:02:45 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:02:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-05-10 23:02:27 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | -0.041 |  |
| 2026-05-10 23:02:19 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:02:07 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:01:54 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-10 23:01:23 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 23:01:22 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2026-05-10 23:01:06 | Wellawaya (Kirindi Oya) | 3.97 | 🟢 Normal | -0.070 |  |
| 2026-05-10 23:00:51 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 22:57:29 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:26:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.033 |  |
| 2026-05-10 22:22:48 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 22:01:18 | Kuda Oya (Kirindi Oya) | 4.41 | 🟢 Normal | 1.417 | 🔺 Rising |
| 2026-05-10 22:02:24 | Thanamalwila (Kirindi Oya) | 2.89 | 🟢 Normal | 0.956 | 🔺 Rising |
| 2026-05-10 23:03:30 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.445 | 🔺 Rising |
| 2026-05-10 22:12:43 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-05-10 22:03:32 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-10 22:01:08 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-10 23:02:56 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-10 22:06:43 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-10 23:01:54 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-10 23:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-10 22:06:48 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-10 23:03:28 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-10 23:01:23 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 23:00:51 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 22:05:46 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 22:04:32 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 22:02:10 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:02:45 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:01:05 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:00:59 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:02:19 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:02:07 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:03:17 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 23:01:22 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:02:13 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:03:33 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:07:02 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:03:20 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-10 23:03:03 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-05-10 22:06:47 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-05-10 23:02:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-05-10 22:26:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.033 |  |
| 2026-05-10 22:00:51 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.035 |  |
| 2026-05-10 23:02:27 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | -0.041 |  |
| 2026-05-10 22:05:28 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.041 |  |
| 2026-05-10 23:01:06 | Wellawaya (Kirindi Oya) | 3.97 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)