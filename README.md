# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_03:36:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,826 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 03:36:11 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-06 03:31:54 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:30:26 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-01-06 03:22:41 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-01-06 03:18:22 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-06 03:14:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-06 03:10:34 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-06 03:10:04 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:10:02 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:09:59 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:08:10 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-01-06 03:07:53 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-01-06 03:07:00 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-01-06 03:05:10 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:04:59 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.143 |  |
| 2026-01-06 03:04:50 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 03:04:30 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.107 |  |
| 2026-01-06 03:04:19 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 03:03:46 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:03:45 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-06 03:03:24 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:02:59 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-06 03:02:56 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:02:48 | Siyambalanduwa (Heda Oya) | 2.20 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-01-06 03:02:23 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 03:02:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-06 03:02:13 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-06 03:01:54 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 03:01:27 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.414 |  |
| 2026-01-06 03:01:22 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:01:14 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.011 |  |
| 2026-01-06 03:00:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.080 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 03:30:26 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-01-06 03:02:48 | Siyambalanduwa (Heda Oya) | 2.20 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-01-06 03:07:53 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-01-06 03:14:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-06 03:02:59 | Manampitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-06 03:02:13 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-06 03:00:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-06 03:03:45 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-06 02:34:27 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-06 02:12:24 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-06 03:18:22 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-06 01:04:02 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 03:02:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-06 03:36:11 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-06 03:10:34 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-06 03:01:54 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 03:04:19 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 03:02:23 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 03:04:50 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 03:01:22 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:05:10 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:10:04 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:26:01 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:04:59 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:03:24 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 02:09:07 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:31:54 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:03:46 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:02:56 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-06 03:22:41 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-01-06 03:07:00 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-06 03:01:14 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.011 |  |
| 2026-01-06 03:04:30 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.107 |  |
| 2026-01-06 03:04:59 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.143 |  |
| 2026-01-06 03:01:27 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.414 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)