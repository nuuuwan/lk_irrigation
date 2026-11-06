# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_15:28:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,527 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 15:28:37 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:11:51 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-11-06 15:11:34 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:09:20 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.018 |  |
| 2026-11-06 15:08:45 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:07:43 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:07:43 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:06:04 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:05:57 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.029 |  |
| 2026-11-06 15:05:55 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:05:50 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:05:20 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-11-06 15:05:15 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-06 15:05:03 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-11-06 15:04:59 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-06 15:04:58 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:04:48 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-11-06 15:04:39 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.039 |  |
| 2026-11-06 15:04:29 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.022 |  |
| 2026-11-06 15:04:24 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.029 |  |
| 2026-11-06 15:04:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.133 |  |
| 2026-11-06 15:04:11 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-06 15:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.99 | 🟢 Normal | -0.059 |  |
| 2026-11-06 15:04:06 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 15:03:54 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.050 |  |
| 2026-11-06 15:03:42 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:03:34 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 15:03:33 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-11-06 15:03:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:02:25 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-11-06 15:02:16 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | -0.065 |  |
| 2026-11-06 15:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:02:04 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:01:56 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-06 15:01:28 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-06 15:01:19 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:01:16 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 15:00:51 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:00:17 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:00:13 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.133 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 15:01:28 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-06 15:01:16 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 15:04:06 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 15:05:15 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-06 15:04:59 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-06 15:01:56 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-06 15:03:34 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 15:03:42 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:02:04 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:07:43 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:07:43 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:05:55 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:06:04 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:03:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:28:37 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:11:34 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:05:50 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-06 15:11:51 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-11-06 15:01:19 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:00:51 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:08:45 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:04:58 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-11-06 15:05:20 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-11-06 15:09:20 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.018 |  |
| 2026-11-06 15:03:33 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-11-06 15:04:11 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-06 15:05:03 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-11-06 15:04:29 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.022 |  |
| 2026-11-06 15:04:48 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-11-06 15:04:24 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.029 |  |
| 2026-11-06 15:05:57 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.029 |  |
| 2026-11-06 15:04:39 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | -0.039 |  |
| 2026-11-06 15:02:25 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-11-06 15:03:54 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.050 |  |
| 2026-11-06 15:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.99 | 🟢 Normal | -0.059 |  |
| 2026-11-06 15:02:16 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | -0.065 |  |
| 2026-11-06 15:04:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.133 |  |
| 2026-11-06 15:00:13 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)