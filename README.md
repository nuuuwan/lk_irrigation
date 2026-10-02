# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_02:32:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 02:32:48 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.005 |  |
| 2026-10-03 02:16:55 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-03 02:09:55 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-03 02:09:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:08:01 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.086 |  |
| 2026-10-03 02:07:46 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:07:26 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-03 02:06:41 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.085 |  |
| 2026-10-03 02:06:36 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-03 02:06:24 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-10-03 02:04:16 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 02:04:11 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -5.538 |  |
| 2026-10-03 02:03:58 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-10-03 02:03:53 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-03 02:03:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:03:15 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-10-03 02:03:04 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-03 02:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -5.538 |  |
| 2026-10-03 02:02:40 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:02:29 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:02:11 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 02:02:07 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:02:06 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:01:56 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.099 |  |
| 2026-10-03 02:01:23 | Ellagawa (Kalu Ganga) | 6.39 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-03 02:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-03 02:01:07 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-03 02:01:03 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.081 |  |
| 2026-10-03 02:00:59 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:00:44 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 01:01:15 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-03 02:16:55 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-03 02:01:23 | Ellagawa (Kalu Ganga) | 6.39 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-03 02:06:36 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-03 02:09:55 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-03 01:02:24 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-03 02:03:53 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-03 01:06:51 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-03 02:04:16 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 02:07:26 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-03 02:02:11 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 02:00:59 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:00:44 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:02:06 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:02:29 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:01:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:03:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:04:11 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:09:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:02:07 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:07:46 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:02:40 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:06:23 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:32:48 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.005 |  |
| 2026-10-03 02:01:07 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-03 02:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 02:06:24 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-10-03 02:03:15 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-10-03 02:03:04 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-03 02:03:58 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-10-03 01:19:05 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.051 |  |
| 2026-10-03 02:01:03 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.081 |  |
| 2026-10-03 02:06:41 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.085 |  |
| 2026-10-03 02:08:01 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.086 |  |
| 2026-10-03 02:01:56 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.099 |  |
| 2026-10-03 02:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -5.538 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)