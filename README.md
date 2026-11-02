# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_19:02:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 19:02:55 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-02 19:02:49 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:34 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.040 |  |
| 2026-11-02 19:02:30 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2026-11-02 19:02:27 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:26 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.069 |  |
| 2026-11-02 19:02:18 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:06 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:04 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:01:53 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 19:01:13 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-02 19:00:29 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:00:25 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 18:25:23 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.026 |  |
| 2026-11-02 18:23:42 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 19:02:55 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-02 18:01:10 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-02 18:07:01 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-02 18:02:01 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-02 18:08:53 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-02 19:00:25 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 18:00:34 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 19:01:53 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 18:05:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 18:23:42 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-02 19:02:04 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:06 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:18 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:38 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:27 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:00:29 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:06:49 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:04:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:20 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:49 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:04:26 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:16 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-02 18:05:55 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-02 19:01:13 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-02 18:02:24 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-11-02 18:25:23 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.026 |  |
| 2026-11-02 19:02:30 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-02 18:02:19 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.033 |  |
| 2026-11-02 18:06:07 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.034 |  |
| 2026-11-02 19:02:34 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.040 |  |
| 2026-11-02 18:12:48 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.043 |  |
| 2026-11-02 18:02:55 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.044 |  |
| 2026-11-02 18:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.050 |  |
| 2026-11-02 19:02:26 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.069 |  |
| 2026-11-02 18:09:05 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)