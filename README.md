# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_05:25:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,410 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 05:25:13 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.089 |  |
| 2026-11-03 05:22:23 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:14:25 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.032 |  |
| 2026-11-03 05:11:13 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.034 |  |
| 2026-11-03 05:09:41 | Horowpothana (Yan Oya) | 3.24 | 🟢 Normal | -0.044 |  |
| 2026-11-03 05:08:53 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.393 |  |
| 2026-11-03 05:08:51 | Moraketiya (Walawe Ganga) | 1.53 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-11-03 05:08:22 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 05:07:34 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:07:15 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-03 05:06:07 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-03 05:06:05 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.037 |  |
| 2026-11-03 05:06:03 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.121 |  |
| 2026-11-03 05:06:03 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.346 |  |
| 2026-11-03 05:05:58 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 05:05:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:05:13 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:04:56 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | 0.715 | 🔺 Rising |
| 2026-11-03 05:04:55 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.071 |  |
| 2026-11-03 05:04:12 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-03 05:04:07 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 05:03:49 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-03 05:03:33 | Giriulla (Maha Oya) | 3.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-03 05:03:24 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.287 |  |
| 2026-11-03 05:03:21 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.482 | 🔺 Rising |
| 2026-11-03 05:03:03 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.138 |  |
| 2026-11-03 05:02:52 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 05:02:17 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.012 |  |
| 2026-11-03 05:02:17 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | -0.150 |  |
| 2026-11-03 05:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-03 05:02:01 | Moragaswewa (Deduru Oya) | 3.20 | 🟢 Normal | 0.896 | 🔺 Rising |
| 2026-11-03 05:01:37 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:01:35 | Rathnapura (Kalu Ganga) | 3.49 | 🟢 Normal | -0.137 |  |
| 2026-11-03 05:01:20 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -0.082 |  |
| 2026-11-03 05:01:05 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 05:02:01 | Moragaswewa (Deduru Oya) | 3.20 | 🟢 Normal | 0.896 | 🔺 Rising |
| 2026-11-03 05:04:56 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | 0.715 | 🔺 Rising |
| 2026-11-03 05:03:21 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.482 | 🔺 Rising |
| 2026-11-03 05:08:51 | Moraketiya (Walawe Ganga) | 1.53 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-11-03 05:04:12 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-03 05:08:22 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 05:03:33 | Giriulla (Maha Oya) | 3.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-03 05:07:15 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-03 05:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-03 05:05:58 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 05:02:52 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 05:06:07 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-03 05:04:07 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 05:05:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:01:37 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:34:42 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:05:13 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:22:23 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 05:03:49 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-03 05:02:17 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.012 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-03 05:14:25 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.032 |  |
| 2026-11-03 05:11:13 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -0.034 |  |
| 2026-11-03 05:06:05 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.037 |  |
| 2026-11-03 05:01:05 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.040 |  |
| 2026-11-03 05:09:41 | Horowpothana (Yan Oya) | 3.24 | 🟢 Normal | -0.044 |  |
| 2026-11-03 05:04:55 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.071 |  |
| 2026-11-03 05:01:20 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -0.082 |  |
| 2026-11-03 05:25:13 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.089 |  |
| 2026-11-03 05:06:03 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.121 |  |
| 2026-11-03 05:01:35 | Rathnapura (Kalu Ganga) | 3.49 | 🟢 Normal | -0.137 |  |
| 2026-11-03 05:03:03 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.138 |  |
| 2026-11-03 05:02:17 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | -0.150 |  |
| 2026-11-03 05:03:24 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.287 |  |
| 2026-11-03 05:06:03 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.346 |  |
| 2026-11-03 05:08:53 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.393 |  |
| 2026-11-03 04:23:40 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -0.470 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)