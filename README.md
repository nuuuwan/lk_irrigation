# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_22:24:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,067 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 22:24:20 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:13:20 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-11-22 22:09:14 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-11-22 22:07:23 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 22:06:51 | Thawalama (Gin Ganga) | 3.15 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-11-22 22:06:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.042 |  |
| 2026-11-22 22:06:39 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.073 |  |
| 2026-11-22 22:06:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-11-22 22:06:02 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.019 |  |
| 2026-11-22 22:05:59 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-11-22 22:05:18 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-11-22 22:05:16 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:03:52 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-11-22 22:03:44 | Moragaswewa (Deduru Oya) | 2.94 | 🟢 Normal | -0.154 |  |
| 2026-11-22 22:03:37 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-22 22:03:17 | Moraketiya (Walawe Ganga) | 2.84 | 🟢 Normal | -0.019 |  |
| 2026-11-22 22:03:16 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.072 |  |
| 2026-11-22 22:03:09 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:03:03 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-11-22 22:02:34 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:02:21 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.102 |  |
| 2026-11-22 22:02:14 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-22 22:02:12 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.043 |  |
| 2026-11-22 22:02:12 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-22 22:01:42 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-22 22:01:41 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:01:24 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:01:21 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:00:57 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:00:38 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-22 22:00:37 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:00:08 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 21:59:07 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 22:06:51 | Thawalama (Gin Ganga) | 3.15 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-11-22 22:03:03 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-11-22 22:03:37 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-22 22:07:23 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 21:14:40 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 22:00:08 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 22:02:34 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:01:24 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:01:21 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 21:02:08 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:24:20 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:03:09 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:00:37 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:05:16 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:00:57 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:01:41 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-22 22:13:20 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-11-22 22:09:14 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-11-22 22:02:14 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-22 22:02:12 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-22 22:00:38 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-22 22:05:59 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-11-22 21:59:07 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-22 22:06:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-11-22 22:03:17 | Moraketiya (Walawe Ganga) | 2.84 | 🟢 Normal | -0.019 |  |
| 2026-11-22 22:06:02 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.019 |  |
| 2026-11-22 22:01:42 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-22 22:05:18 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-11-22 22:03:52 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-11-22 22:06:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.042 |  |
| 2026-11-22 22:02:12 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.043 |  |
| 2026-11-22 22:03:16 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.072 |  |
| 2026-11-22 22:06:39 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.073 |  |
| 2026-11-22 22:02:21 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.102 |  |
| 2026-11-22 22:03:44 | Moragaswewa (Deduru Oya) | 2.94 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)