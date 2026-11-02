# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_16:13:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 16:13:34 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:12:13 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.055 |  |
| 2026-11-02 16:10:45 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.049 |  |
| 2026-11-02 16:09:09 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-11-02 16:08:32 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-11-02 16:08:26 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-11-02 16:07:28 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:07:19 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:07:15 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:07:11 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:07:10 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-11-02 16:06:40 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:06:21 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:06:16 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-02 16:06:12 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:06:00 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.028 |  |
| 2026-11-02 16:05:18 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | -0.039 |  |
| 2026-11-02 16:04:26 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:04:08 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-02 16:04:08 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.059 |  |
| 2026-11-02 16:04:05 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:03:56 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-11-02 16:03:15 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:03:00 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-11-02 16:02:41 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:02:39 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-02 16:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.050 |  |
| 2026-11-02 16:02:09 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.087 |  |
| 2026-11-02 16:02:08 | Moragaswewa (Deduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:02:02 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:51 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-11-02 16:01:49 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-02 16:01:33 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:21 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:12 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 16:01:03 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:01 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:00:13 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 16:09:09 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-11-02 16:08:26 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-11-02 16:04:08 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-02 16:02:39 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-02 16:01:12 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 16:01:21 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:02:08 | Moragaswewa (Deduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:13:34 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:33 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:04:05 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:02:41 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:03:15 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:02:02 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:07:11 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:01 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:06:12 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:06:21 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:03 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:01:49 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-02 16:08:32 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-11-02 16:06:16 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-02 16:03:00 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-11-02 16:01:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-11-02 16:04:26 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:07:15 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:06:40 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:07:28 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:00:13 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:07:19 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:06:00 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.028 |  |
| 2026-11-02 16:03:56 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-11-02 16:07:10 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2026-11-02 16:05:18 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | -0.039 |  |
| 2026-11-02 16:01:51 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-11-02 16:10:45 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.049 |  |
| 2026-11-02 16:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.050 |  |
| 2026-11-02 16:12:13 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.055 |  |
| 2026-11-02 16:04:08 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.059 |  |
| 2026-11-02 16:02:09 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)