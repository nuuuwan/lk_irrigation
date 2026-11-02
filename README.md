# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_07:04:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 07:04:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:03:54 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.021 |  |
| 2026-11-02 07:03:23 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 07:03:05 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-02 07:02:47 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-11-02 07:02:46 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:02:41 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 07:02:23 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 07:02:19 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-02 07:02:03 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-02 07:01:58 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.049 |  |
| 2026-11-02 07:01:53 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:01:50 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-11-02 07:01:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:01:29 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-02 07:01:10 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.114 |  |
| 2026-11-02 07:01:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-02 07:01:07 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-11-02 07:00:51 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-11-02 07:00:49 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.022 |  |
| 2026-11-02 07:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:36:40 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 07:02:03 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-02 07:02:19 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-02 07:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 07:03:05 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-02 07:02:41 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 06:07:41 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-02 07:02:23 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 06:03:37 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-02 06:05:50 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-02 07:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:01:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:03:23 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:01:53 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:02:46 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:16:46 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:06:49 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:02:47 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:04:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:01:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 06:02:36 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:01:50 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-11-02 07:01:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-02 06:01:24 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-11-02 07:00:51 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-11-02 06:11:33 | Thalgahagoda (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.018 |  |
| 2026-11-02 06:06:59 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-02 07:01:07 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-11-02 07:02:47 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-11-02 07:03:54 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.021 |  |
| 2026-11-02 07:00:49 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.022 |  |
| 2026-11-02 06:02:43 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-11-02 07:01:29 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-11-02 07:01:58 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.049 |  |
| 2026-11-02 06:02:51 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.073 |  |
| 2026-11-02 06:04:03 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.079 |  |
| 2026-11-02 06:01:52 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.102 |  |
| 2026-11-02 07:01:10 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.114 |  |
| 2026-11-02 06:00:23 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)