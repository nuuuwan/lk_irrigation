# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_23:03:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,181 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 23:03:27 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:03:27 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-02 23:03:08 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.030 |  |
| 2026-11-02 23:02:40 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:02:25 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-02 23:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.020 |  |
| 2026-11-02 23:02:09 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-02 23:01:31 | Padiyathalawa (Maduru Oya) | 1.92 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-02 23:01:22 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.099 |  |
| 2026-11-02 23:01:08 | Panadugama (Nilwala Ganga) | 4.32 | 🟢 Normal | -0.042 |  |
| 2026-11-02 23:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 23:01:04 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-11-02 23:00:21 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.011 |  |
| 2026-11-02 23:00:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:00:10 | Wellawaya (Kirindi Oya) | 2.80 | 🟢 Normal | -0.213 |  |
| 2026-11-02 22:49:15 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.012 |  |
| 2026-11-02 22:37:23 | Holombuwa (Kelani Ganga) | 2.10 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-11-02 22:27:41 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.007 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 22:10:55 | Thaldena (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.626 | 🔺 Rising |
| 2026-11-02 22:10:41 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-11-02 22:37:23 | Holombuwa (Kelani Ganga) | 2.10 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-11-02 23:01:04 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-11-02 23:03:27 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-02 23:01:31 | Padiyathalawa (Maduru Oya) | 1.92 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-02 22:01:09 | Peradeniya (Mahaweli Ganga) | 3.84 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-02 23:02:25 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-02 22:02:51 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-02 22:04:34 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 23:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 22:27:41 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-02 23:00:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:02:40 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:01:53 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:03:27 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:04:08 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:04:45 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:10:37 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:08:15 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:00:15 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:06:42 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:06:37 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-11-02 23:02:09 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-02 23:00:21 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.011 |  |
| 2026-11-02 22:49:15 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.012 |  |
| 2026-11-02 23:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.020 |  |
| 2026-11-02 22:11:50 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-11-02 23:03:08 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.030 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-02 23:01:08 | Panadugama (Nilwala Ganga) | 4.32 | 🟢 Normal | -0.042 |  |
| 2026-11-02 22:06:35 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.047 |  |
| 2026-11-02 22:06:46 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.063 |  |
| 2026-11-02 22:01:09 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.087 |  |
| 2026-11-02 23:01:22 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.099 |  |
| 2026-11-02 23:00:10 | Wellawaya (Kirindi Oya) | 2.80 | 🟢 Normal | -0.213 |  |
| 2026-11-02 22:04:02 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.306 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)