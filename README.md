# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_03:03:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,309 measurements** from **39** stations.
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
| 2026-11-03 03:03:01 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 03:02:57 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-03 03:02:18 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 03:02:07 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.110 |  |
| 2026-11-03 03:02:03 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:57 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:57 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:55 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:52 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:31 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.156 |  |
| 2026-11-03 03:00:16 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-03 03:00:08 | Siyambalanduwa (Heda Oya) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 02:26:14 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.372 |  |
| 2026-11-03 02:23:09 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 02:14:33 | Horowpothana (Yan Oya) | 3.27 | 🟢 Normal | 5.806 | 🔺 Rising |
| 2026-11-03 02:05:33 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | 0.876 | 🔺 Rising |
| 2026-11-03 02:02:10 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-11-03 00:08:45 | Padiyathalawa (Maduru Oya) | 2.41 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-11-03 00:15:17 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-11-03 02:03:55 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-03 02:05:47 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-03 03:02:57 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 02:10:01 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-03 02:02:54 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-03 03:00:08 | Siyambalanduwa (Heda Oya) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 03:02:18 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 03:03:01 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 02:08:05 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:02:03 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:21:44 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:57 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:52 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:57 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-03 02:13:10 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-11-03 02:04:56 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-11-03 02:04:33 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-11-03 03:00:16 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-03 02:05:20 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-11-03 02:01:12 | Peradeniya (Mahaweli Ganga) | 4.40 | 🟢 Normal | -0.021 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-03 02:07:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-11-03 00:03:19 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.039 |  |
| 2026-11-03 02:04:02 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.090 |  |
| 2026-11-03 02:07:23 | Rathnapura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.095 |  |
| 2026-11-03 03:02:07 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.110 |  |
| 2026-11-03 03:01:31 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.156 |  |
| 2026-11-03 02:00:11 | Wellawaya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.311 |  |
| 2026-11-03 02:26:14 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.372 |  |
| 2026-11-03 02:03:22 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -1.241 |  |
| 2026-11-03 02:05:00 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)