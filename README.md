# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_04:10:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 04:10:52 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.013 |  |
| 2026-11-20 04:07:19 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-20 04:07:05 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.003 |  |
| 2026-11-20 04:06:34 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:05:58 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:05:40 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:05:19 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:05:04 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-20 04:04:53 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.045 |  |
| 2026-11-20 04:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:04:08 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:03:47 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-11-20 04:03:12 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.071 |  |
| 2026-11-20 04:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-20 04:02:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-20 04:02:41 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:02:37 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-20 04:02:20 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:02:07 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:56 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 04:01:56 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:56 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:35 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:17 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-11-20 04:01:08 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:07 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:00:56 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:00:33 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:00:10 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 04:01:17 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-11-20 04:02:37 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-20 04:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-20 04:02:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-20 04:05:04 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-20 03:01:47 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 04:01:56 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 04:07:19 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-19 18:00:52 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:07 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:35 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:05:19 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-20 03:07:06 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:08 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:06:34 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:38:53 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:56 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:01:56 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:00:33 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:04:08 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:05:40 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-19 18:01:52 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:03:59 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:02:07 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:07:05 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.003 |  |
| 2026-11-20 03:25:58 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-11-19 18:05:17 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-11-20 04:02:41 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:05:58 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:02:20 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:00:56 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:00:10 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-20 04:10:52 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.013 |  |
| 2026-11-20 03:03:58 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-11-20 04:03:47 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-11-20 04:04:53 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.045 |  |
| 2026-11-20 04:03:12 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)