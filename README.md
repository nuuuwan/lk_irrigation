# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_11:32:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,694 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 11:32:00 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:23:29 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.022 |  |
| 2026-09-13 11:22:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:17:59 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:16:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-13 11:15:20 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-13 11:11:08 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-13 11:09:34 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 11:09:30 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:09:22 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-09-13 11:09:09 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.028 |  |
| 2026-09-13 11:07:37 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:07:11 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:07:02 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:06:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-13 11:05:03 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-09-13 11:04:53 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | -0.075 |  |
| 2026-09-13 11:04:52 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:03:51 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:03:42 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:03:16 | Magura (Kalu Ganga) | 3.53 | 🟢 Normal | -0.085 |  |
| 2026-09-13 11:03:02 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-09-13 11:02:51 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:39 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-09-13 11:02:33 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:28 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:24 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:22 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:18 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-13 11:02:08 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-13 11:02:05 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:04 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:00 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:01:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:01:23 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-13 11:01:16 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.159 |  |
| 2026-09-13 11:01:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:00:45 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:00:36 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-13 11:00:07 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 11:03:02 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-09-13 11:01:23 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-13 11:02:08 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-13 11:06:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-13 11:11:08 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-13 11:16:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-13 11:09:34 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 11:02:00 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:03:42 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:03:51 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:01:34 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:09:30 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:00:45 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:22:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:32:00 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:24 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:07:37 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:33 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:07:11 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:22 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:51 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:04:52 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:28 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:01:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:17:59 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:02:05 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:15:20 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-13 11:00:36 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-13 11:00:07 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-09-13 11:02:18 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-13 11:23:29 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.022 |  |
| 2026-09-13 11:09:09 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.028 |  |
| 2026-09-13 11:05:03 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-09-13 11:09:22 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-09-13 11:02:39 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-09-13 11:04:53 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | -0.075 |  |
| 2026-09-13 11:03:16 | Magura (Kalu Ganga) | 3.53 | 🟢 Normal | -0.085 |  |
| 2026-09-13 11:01:16 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)