# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_20:02:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 20:02:55 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:02:27 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-11-22 20:02:24 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.050 |  |
| 2026-11-22 20:02:13 | Moraketiya (Walawe Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:02:06 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.043 |  |
| 2026-11-22 20:01:53 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 20:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:01:37 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-11-22 20:01:15 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 20:01:15 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 20:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-22 20:00:45 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.105 |  |
| 2026-11-22 20:00:34 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 19:17:03 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-22 19:04:02 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-22 19:06:09 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 20:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-22 20:01:15 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 20:01:53 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 19:04:09 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 19:06:59 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-22 20:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:00:34 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:02:21 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:02:06 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:03:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:02:13 | Moraketiya (Walawe Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-11-22 20:02:55 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:05:22 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:04:10 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-22 19:16:08 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:01:57 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-22 20:01:15 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:00:49 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-22 19:06:22 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.011 |  |
| 2026-11-22 19:00:07 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-11-22 20:01:37 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-22 19:07:33 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.028 |  |
| 2026-11-22 19:05:12 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-11-22 19:02:46 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-11-22 20:02:27 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-11-22 20:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.043 |  |
| 2026-11-22 19:07:21 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.045 |  |
| 2026-11-22 20:02:24 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.050 |  |
| 2026-11-22 19:03:14 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.052 |  |
| 2026-11-22 19:11:14 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.052 |  |
| 2026-11-22 20:00:45 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.105 |  |
| 2026-11-22 19:02:43 | Moragaswewa (Deduru Oya) | 3.31 | 🟢 Normal | -0.241 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)