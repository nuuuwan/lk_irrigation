# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_02:03:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,275 measurements** from **39** stations.
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
| 2026-11-03 02:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.072 |  |
| 2026-11-03 02:02:54 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-03 02:02:53 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 02:02:29 | Glencourse (Kelani Ganga) | 11.99 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-11-03 02:02:10 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-11-03 02:01:56 | Nakkala (Kumbukkan Oya) | 2.06 | 🟢 Normal | 1854.000 | 🔺 Rising |
| 2026-11-03 02:01:54 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 1854.000 | 🔺 Rising |
| 2026-11-03 02:01:47 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 02:01:41 | Siyambalanduwa (Heda Oya) | 1.41 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-11-03 02:01:26 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.047 |  |
| 2026-11-03 02:01:21 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-03 02:01:12 | Peradeniya (Mahaweli Ganga) | 4.40 | 🟢 Normal | -0.021 |  |
| 2026-11-03 02:00:11 | Wellawaya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.311 |  |
| 2026-11-03 01:48:42 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 02:01:56 | Nakkala (Kumbukkan Oya) | 2.06 | 🟢 Normal | 1854.000 | 🔺 Rising |
| 2026-11-03 02:02:10 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-11-03 00:08:45 | Padiyathalawa (Maduru Oya) | 2.41 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-11-03 02:01:41 | Siyambalanduwa (Heda Oya) | 1.41 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-11-03 01:05:08 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-11-03 00:15:17 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-11-03 02:02:29 | Glencourse (Kelani Ganga) | 11.99 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-11-03 01:01:52 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-03 00:00:13 | Horowpothana (Yan Oya) | 3.18 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 02:02:54 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-03 01:03:54 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 01:06:53 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-03 02:02:53 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 01:04:34 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 01:07:55 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:02:16 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-03 02:01:47 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:13:37 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:13:35 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:02:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:21:44 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:05:55 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-11-03 02:01:21 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-03 01:04:54 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-03 01:07:03 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-11-03 02:01:12 | Peradeniya (Mahaweli Ganga) | 4.40 | 🟢 Normal | -0.021 |  |
| 2026-11-03 01:10:37 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.027 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-03 00:03:19 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.039 |  |
| 2026-11-03 02:01:26 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.047 |  |
| 2026-11-03 02:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.072 |  |
| 2026-11-03 01:04:18 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.119 |  |
| 2026-11-03 01:01:14 | Thaldena (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.120 |  |
| 2026-11-03 01:03:43 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.140 |  |
| 2026-11-03 02:00:11 | Wellawaya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.311 |  |
| 2026-11-03 01:08:49 | Holombuwa (Kelani Ganga) | 2.22 | 🟢 Normal | -0.374 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)