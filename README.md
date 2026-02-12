# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_05:09:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,633 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 05:09:03 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.090 |  |
| 2026-02-13 05:09:01 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 05:06:59 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:06:23 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 05:05:59 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:05:22 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:05:19 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-02-13 05:04:59 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-13 05:04:25 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-13 05:02:51 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:02:41 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:02:38 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.441 | 🔺 Rising |
| 2026-02-13 05:02:35 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:02:33 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-13 05:02:32 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:02:30 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.015 |  |
| 2026-02-13 05:02:27 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-02-13 05:02:00 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-02-13 05:01:43 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:01:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:01:36 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2026-02-13 05:01:32 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:01:13 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:00:43 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:00:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 04:43:53 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:33:34 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 04:32:50 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 04:30:09 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 04:29:46 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 04:26:02 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:23:19 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.015 |  |
| 2026-02-13 04:21:06 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-02-13 04:19:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 04:18:08 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:17:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:17:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 05:02:38 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.441 | 🔺 Rising |
| 2026-02-13 05:02:27 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-02-13 05:04:59 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-13 03:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-13 05:02:33 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-13 05:06:23 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-13 04:14:49 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-13 04:08:46 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-13 05:04:25 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-13 04:17:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-13 05:00:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:02:35 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:01:13 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:02:32 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:05:22 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 05:09:01 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 04:01:13 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:00:43 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:01:43 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:02:09 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:02:51 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:17:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:05:59 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:02:41 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:06:59 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:01:32 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:43:53 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 05:01:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:02:56 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-02-13 05:02:30 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.015 |  |
| 2026-02-13 05:05:19 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-02-13 04:11:12 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-02-13 05:01:36 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2026-02-13 05:02:00 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-02-13 04:02:13 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.062 |  |
| 2026-02-13 05:09:03 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)