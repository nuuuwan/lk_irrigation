# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_19:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,654 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 19:03:25 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 19:03:06 | Nawalapitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.636 | 🔺 Rising |
| 2026-11-06 19:03:05 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-06 19:03:04 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-11-06 19:02:37 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 19:02:15 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 19:01:08 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-06 19:00:49 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-06 19:00:48 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-06 18:53:38 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.075 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 19:03:06 | Nawalapitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.636 | 🔺 Rising |
| 2026-11-06 18:08:15 | Holombuwa (Kelani Ganga) | 2.34 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-11-06 18:04:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-11-06 18:02:51 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-11-06 19:01:08 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-06 18:02:59 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-06 18:53:38 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-06 18:03:01 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-06 19:02:15 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 18:07:20 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-06 18:04:33 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-06 18:05:54 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-06 19:00:48 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-06 19:00:49 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-06 18:01:23 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 19:03:25 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 18:02:28 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 17:07:21 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 18:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:04:38 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:20 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:16:04 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:04:32 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:01:42 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:02:36 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 19:03:05 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-06 18:04:01 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-11-06 19:02:37 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 18:06:58 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-11-06 18:05:26 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-11-06 19:03:04 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-11-06 18:01:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.034 |  |
| 2026-11-06 18:03:28 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.047 |  |
| 2026-11-06 18:02:39 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.070 |  |
| 2026-11-06 18:03:05 | Moragaswewa (Deduru Oya) | 2.43 | 🟢 Normal | -0.078 |  |
| 2026-11-06 18:05:52 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)