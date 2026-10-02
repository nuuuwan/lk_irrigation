# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_01:06:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,325 measurements** from **39** stations.
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
| 2026-10-03 01:06:23 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:06:17 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-03 01:05:52 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-03 01:05:48 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-03 01:05:34 | Kithulgala (Kelani Ganga) | 2.28 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-03 01:05:30 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:05:00 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:03:25 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 01:03:20 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:03:14 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:03:09 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 01:03:09 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-10-03 01:02:58 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-10-03 01:02:58 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.042 |  |
| 2026-10-03 01:02:32 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-10-03 01:02:26 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:02:24 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-03 01:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-10-03 01:01:40 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-03 01:01:32 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.080 |  |
| 2026-10-03 01:01:31 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-03 01:01:22 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:01:15 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-03 01:01:02 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -90.000 |  |
| 2026-10-03 01:01:00 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -90.000 |  |
| 2026-10-03 01:00:38 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:00:26 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:59:45 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:58:58 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:52:08 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:24:54 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.027 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 01:01:15 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-03 01:05:48 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-03 00:10:30 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-03 01:01:40 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-03 01:05:52 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-03 01:05:34 | Kithulgala (Kelani Ganga) | 2.28 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-03 01:06:17 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-03 01:02:24 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-03 00:24:54 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-03 01:03:25 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 01:01:31 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-03 01:03:09 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 01:00:26 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:01:22 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:02:26 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:05:30 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:01:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:00:38 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:03:20 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:03:14 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:05:00 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:04:11 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:52:08 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:06:23 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-10-03 00:08:34 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 00:20:12 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.016 |  |
| 2026-10-03 01:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-10-03 01:03:09 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-10-03 01:02:58 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-10-03 01:02:32 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-10-03 01:02:58 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.042 |  |
| 2026-10-03 00:20:03 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | -0.070 |  |
| 2026-10-03 01:01:32 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.080 |  |
| 2026-10-03 00:03:31 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -2.028 |  |
| 2026-10-03 01:01:02 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)