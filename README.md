# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_23:06:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,371 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 23:06:17 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:05:58 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:05:19 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:05:16 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:05:15 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-02-22 23:04:44 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:04:11 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-02-22 23:03:58 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:03:51 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-02-22 23:03:48 | Manampitiya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.133 |  |
| 2026-02-22 23:03:19 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-02-22 23:03:05 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.064 |  |
| 2026-02-22 23:03:04 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -252.000 |  |
| 2026-02-22 23:03:03 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -252.000 |  |
| 2026-02-22 23:02:39 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:02:35 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.114 |  |
| 2026-02-22 23:02:31 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:02:28 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.408 |  |
| 2026-02-22 23:02:09 | Ellagawa (Kalu Ganga) | 7.47 | 🟢 Normal | -0.276 |  |
| 2026-02-22 23:02:05 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:01:48 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-22 23:01:36 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-02-22 23:01:26 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.053 |  |
| 2026-02-22 23:01:12 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 23:00:45 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:00:45 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.034 |  |
| 2026-02-22 23:00:35 | Padiyathalawa (Maduru Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-02-22 22:53:39 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | -0.408 |  |
| 2026-02-22 22:46:57 | Ellagawa (Kalu Ganga) | 7.54 | 🟢 Normal | -0.276 |  |
| 2026-02-22 22:25:11 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.034 |  |
| 2026-02-22 22:16:25 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 23:04:11 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-02-22 23:01:36 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-02-22 23:01:48 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 23:01:12 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 23:04:44 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:06:24 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:02:05 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:00:45 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:05:19 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:04:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:06:17 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 23:02:39 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:11:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-02-22 22:11:58 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:03:58 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:05:16 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:02:31 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-22 22:00:54 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:05:58 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-22 23:00:35 | Padiyathalawa (Maduru Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-02-22 23:03:51 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-02-22 23:03:19 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-02-22 22:05:31 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.025 |  |
| 2026-02-22 22:06:15 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.028 |  |
| 2026-02-22 23:05:15 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-02-22 23:00:45 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.034 |  |
| 2026-02-22 23:01:26 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.053 |  |
| 2026-02-22 22:08:51 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.061 |  |
| 2026-02-22 23:03:05 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.064 |  |
| 2026-02-22 22:05:29 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.067 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-22 23:02:35 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.114 |  |
| 2026-02-22 23:03:48 | Manampitiya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.133 |  |
| 2026-02-22 22:03:44 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.133 |  |
| 2026-02-22 23:02:09 | Ellagawa (Kalu Ganga) | 7.47 | 🟢 Normal | -0.276 |  |
| 2026-02-22 23:02:28 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.408 |  |
| 2026-02-22 23:03:04 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)