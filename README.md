# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_11:32:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,024 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 11:32:47 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:09:02 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.119 |  |
| 2026-05-09 11:08:36 | Galgamuwa (Mee Oya) | 2.69 | 🟢 Normal | -0.048 |  |
| 2026-05-09 11:07:41 | Katharagama (Menik Ganga) | 2.42 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-09 11:07:32 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-05-09 11:07:30 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.058 |  |
| 2026-05-09 11:07:08 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | -0.047 |  |
| 2026-05-09 11:06:34 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.025 |  |
| 2026-05-09 11:06:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | -0.037 |  |
| 2026-05-09 11:06:20 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-05-09 11:05:44 | Moragaswewa (Deduru Oya) | 3.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 11:05:26 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:05:26 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.053 |  |
| 2026-05-09 11:05:23 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-09 11:05:17 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 11:05:06 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.061 |  |
| 2026-05-09 11:04:57 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.028 |  |
| 2026-05-09 11:04:57 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 11:04:44 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-05-09 11:04:29 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 11:04:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-09 11:03:14 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.053 |  |
| 2026-05-09 11:03:14 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-05-09 11:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-09 11:02:47 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:02:34 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.179 |  |
| 2026-05-09 11:02:32 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.041 |  |
| 2026-05-09 11:02:14 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:02:04 | Kuda Oya (Kirindi Oya) | 2.72 | 🟢 Normal | -0.156 |  |
| 2026-05-09 11:02:01 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.063 |  |
| 2026-05-09 11:01:50 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 11:01:47 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-05-09 11:01:38 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:01:25 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 11:01:08 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.075 |  |
| 2026-05-09 11:01:06 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 11:01:04 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 11:00:30 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-09 10:59:32 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 11:07:32 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-05-09 11:07:41 | Katharagama (Menik Ganga) | 2.42 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-09 11:05:23 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-09 11:04:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-09 11:04:57 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 11:05:44 | Moragaswewa (Deduru Oya) | 3.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 11:05:17 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 11:01:06 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 11:04:29 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 11:01:50 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 11:01:25 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 11:01:04 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 11:02:14 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:05:26 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:02:47 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:00:30 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:01:38 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:32:47 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 11:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-09 11:01:47 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-05-09 10:59:32 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.020 |  |
| 2026-05-09 11:06:34 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.025 |  |
| 2026-05-09 11:04:57 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.028 |  |
| 2026-05-09 11:04:44 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-05-09 11:06:20 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-05-09 11:06:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | -0.037 |  |
| 2026-05-09 11:02:32 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.041 |  |
| 2026-05-09 11:03:14 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-05-09 11:07:08 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | -0.047 |  |
| 2026-05-09 11:08:36 | Galgamuwa (Mee Oya) | 2.69 | 🟢 Normal | -0.048 |  |
| 2026-05-09 11:03:14 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.053 |  |
| 2026-05-09 11:05:26 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.053 |  |
| 2026-05-09 11:07:30 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.058 |  |
| 2026-05-09 11:05:06 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.061 |  |
| 2026-05-09 11:02:01 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.063 |  |
| 2026-05-09 11:01:08 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.075 |  |
| 2026-05-09 11:09:02 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.119 |  |
| 2026-05-09 11:02:04 | Kuda Oya (Kirindi Oya) | 2.72 | 🟢 Normal | -0.156 |  |
| 2026-05-09 11:02:34 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)