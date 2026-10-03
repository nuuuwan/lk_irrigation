# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_04:33:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,335 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 04:33:04 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-04 04:30:18 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-04 04:17:53 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.075 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 04:04:42 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-04 04:17:53 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-04 04:08:25 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-04 04:03:30 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-04 04:06:34 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-04 03:16:53 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 04:03:36 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 01:03:34 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 02:02:29 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 04:01:20 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 04:30:18 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-04 04:33:04 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-04 04:00:50 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:01:50 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-04 01:03:41 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:10:28 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:03:28 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:02:39 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:05:55 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:07:06 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:04:17 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:12:05 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:07:48 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 04:01:09 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.005 |  |
| 2026-10-04 04:16:17 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.008 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-04 04:02:11 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-10-04 04:02:47 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.020 |  |
| 2026-10-04 04:05:40 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.024 |  |
| 2026-10-04 04:03:06 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.040 |  |
| 2026-10-04 04:05:18 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.043 |  |
| 2026-10-04 04:04:12 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.056 |  |
| 2026-10-04 04:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.065 |  |
| 2026-10-04 04:02:36 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.119 |  |
| 2026-10-04 04:01:26 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.132 |  |
| 2026-10-04 04:04:44 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)