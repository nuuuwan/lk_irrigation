# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_02:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,670 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 02:17:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-08-01 02:16:51 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-01 02:12:02 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:11:55 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-08-01 02:11:39 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:11:11 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-08-01 02:08:05 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:07:36 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-08-01 02:07:18 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-08-01 02:06:49 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-08-01 02:06:46 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2026-08-01 02:06:07 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 02:05:45 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | 1.278 | 🔺 Rising |
| 2026-08-01 02:05:02 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-08-01 02:04:58 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 02:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.880 | 🔺 Rising |
| 2026-08-01 02:04:18 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 02:04:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:03:28 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:03:06 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-01 02:03:03 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:02:58 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:02:37 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:02:23 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:01:42 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:01:37 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-01 02:01:31 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:01:22 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:01:12 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 1.463 | 🔺 Rising |
| 2026-08-01 02:00:45 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 01:58:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.880 | 🔺 Rising |
| 2026-08-01 01:57:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | 0.880 | 🔺 Rising |
| 2026-08-01 01:56:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.880 | 🔺 Rising |
| 2026-08-01 01:41:31 | Wellawaya (Kirindi Oya) | 0.00 | 🟢 Normal | 1.463 | 🔺 Rising |
| 2026-08-01 01:29:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-08-01 01:29:05 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.154 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 02:01:12 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 1.463 | 🔺 Rising |
| 2026-08-01 02:05:45 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | 1.278 | 🔺 Rising |
| 2026-08-01 02:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.880 | 🔺 Rising |
| 2026-08-01 02:07:36 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-08-01 02:06:49 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-08-01 02:11:11 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-08-01 02:17:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-08-01 02:07:18 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-08-01 02:11:55 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-08-01 02:05:02 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-08-01 01:29:05 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-08-01 02:01:37 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-01 02:03:06 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-01 01:01:27 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-01 02:06:07 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 02:16:51 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-01 02:04:18 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 02:04:58 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 18:04:08 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:00:45 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:02:37 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:04:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 00:02:04 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 01:10:48 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 23:03:12 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:04:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:02:23 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-01 01:01:42 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:08:05 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:12:02 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:02:58 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:01:22 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:05 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:03:28 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:01:31 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:01:42 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-01 02:06:46 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2026-08-01 01:26:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.037 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)