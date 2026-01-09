# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_07:17:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,670 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 07:17:22 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.003 |  |
| 2026-01-09 07:12:51 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:12:01 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.042 |  |
| 2026-01-09 07:10:41 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:09:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:08:39 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:08:32 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-01-09 07:07:09 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-09 07:06:51 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 07:06:45 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:06:22 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 07:05:28 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:05:27 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-09 07:05:13 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 07:04:58 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 07:04:53 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.019 |  |
| 2026-01-09 07:04:41 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:03:53 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-09 07:03:53 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:03:18 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:03:03 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:02:45 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-09 07:02:42 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.071 |  |
| 2026-01-09 07:02:39 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.080 |  |
| 2026-01-09 07:02:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.099 |  |
| 2026-01-09 07:02:20 | Weraganthota (Mahaweli Ganga) | -1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 07:02:14 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-09 07:02:09 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-01-09 07:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.084 |  |
| 2026-01-09 07:01:50 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-09 07:01:24 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:01:22 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 07:01:01 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:00:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:26:29 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 07:02:45 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-09 06:07:03 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-09 07:05:27 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-09 07:02:14 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-09 07:06:22 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 07:06:51 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 07:07:09 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-09 07:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 07:04:58 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 07:02:20 | Weraganthota (Mahaweli Ganga) | -1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 07:05:13 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 07:09:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:02:48 | Moragaswewa (Deduru Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:02:05 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:12:51 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:05:28 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:06:45 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:01:24 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:01:22 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:00:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:01:01 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:08:39 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:03:53 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:04:00 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:03:03 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:03:18 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:04:41 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 07:17:22 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.003 |  |
| 2026-01-09 07:08:32 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-01-09 07:03:53 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-09 07:01:50 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-09 06:08:52 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-01-09 07:04:53 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.019 |  |
| 2026-01-09 07:02:09 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-01-09 07:12:01 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.042 |  |
| 2026-01-09 07:02:42 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.071 |  |
| 2026-01-09 07:02:39 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.080 |  |
| 2026-01-09 07:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.084 |  |
| 2026-01-09 07:02:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)