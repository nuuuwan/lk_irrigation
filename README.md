# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_06:33:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,613 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 06:33:20 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:25:41 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.040 |  |
| 2026-10-02 06:10:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-10-02 06:08:08 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | -0.049 |  |
| 2026-10-02 06:06:43 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.295 |  |
| 2026-10-02 06:06:42 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-02 06:05:41 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:05:07 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-02 06:04:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:04:13 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.107 |  |
| 2026-10-02 06:04:12 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-10-02 06:03:59 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.096 |  |
| 2026-10-02 06:03:56 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:03:48 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:03:28 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:03:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:03:13 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.085 |  |
| 2026-10-02 06:03:02 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.072 |  |
| 2026-10-02 06:02:59 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:02:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 06:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-02 06:02:36 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-02 06:01:59 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-10-02 06:01:57 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:01:51 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.177 |  |
| 2026-10-02 06:01:51 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-10-02 06:01:47 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 06:01:38 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 06:01:34 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-02 06:01:30 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.041 |  |
| 2026-10-02 06:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:01:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-02 06:01:18 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:01:16 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:00:56 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-02 06:00:53 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:00:53 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.072 |  |
| 2026-10-02 06:00:31 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 06:00:56 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-02 06:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-02 06:01:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-02 06:01:34 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-02 06:01:38 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 06:02:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 06:02:36 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-02 06:06:42 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-02 06:01:47 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 06:01:57 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:01:18 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:03:56 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:03:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:00:53 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:33:20 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:05:41 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:03:48 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:03:28 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:04:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:02:59 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:01:16 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 06:05:07 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-10-02 06:00:31 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-10-02 06:04:12 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-10-02 06:01:51 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-10-02 06:01:59 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-10-02 06:10:02 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.029 |  |
| 2026-10-02 06:25:41 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.040 |  |
| 2026-10-02 06:01:30 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.041 |  |
| 2026-10-02 06:08:08 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | -0.049 |  |
| 2026-10-02 06:03:02 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.072 |  |
| 2026-10-02 06:00:53 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.072 |  |
| 2026-10-02 06:03:13 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.085 |  |
| 2026-10-02 06:03:59 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.096 |  |
| 2026-10-02 06:04:13 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.107 |  |
| 2026-10-02 06:01:51 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.177 |  |
| 2026-10-02 06:06:43 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.295 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)