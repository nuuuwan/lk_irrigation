# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_20:09:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,152 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 20:09:32 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.036 |  |
| 2026-10-02 20:08:04 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-02 20:07:51 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-02 20:07:36 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.081 |  |
| 2026-10-02 20:06:55 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:06:44 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-02 20:05:52 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 20:05:46 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 20:05:40 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.399 | 🔺 Rising |
| 2026-10-02 20:05:24 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-10-02 20:05:08 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-02 20:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:04:10 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:03:51 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.029 |  |
| 2026-10-02 20:03:43 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:03:42 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-02 20:03:41 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-10-02 20:03:28 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:03:18 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-02 20:03:12 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-02 20:03:02 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 20:02:54 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.052 |  |
| 2026-10-02 20:02:49 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:02:39 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.067 |  |
| 2026-10-02 20:02:33 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.051 |  |
| 2026-10-02 20:02:24 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:02:03 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:02:00 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-02 20:01:58 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:01:45 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-10-02 20:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-10-02 20:01:36 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-02 20:01:33 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-02 20:01:31 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:01:31 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:00:16 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 20:05:40 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.399 | 🔺 Rising |
| 2026-10-02 20:01:45 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-10-02 20:03:42 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-02 20:01:33 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-02 20:05:08 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-02 20:07:51 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-02 20:08:04 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-02 20:03:18 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-02 20:03:02 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 20:05:46 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 20:05:52 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 20:00:16 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:02:49 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:01:31 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:02:03 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:04:10 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:03:43 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:01:58 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:06:55 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:01:31 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:02:24 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:03:28 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:04:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-02 20:02:00 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-02 20:01:36 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-02 20:03:12 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-02 20:05:24 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-10-02 20:06:44 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-02 20:03:41 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-10-02 20:03:51 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.029 |  |
| 2026-10-02 20:09:32 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.036 |  |
| 2026-10-02 20:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-10-02 20:02:33 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.051 |  |
| 2026-10-02 20:02:54 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.052 |  |
| 2026-10-02 20:02:39 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.067 |  |
| 2026-10-02 20:07:36 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)