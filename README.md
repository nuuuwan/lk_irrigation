# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_15:17:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,172 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 15:17:07 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:15:56 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:15:41 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:12:44 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:12:31 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:09:38 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-04-21 15:07:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-21 15:07:23 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-21 15:06:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-21 15:06:36 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-21 15:06:36 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:05:59 | Galgamuwa (Mee Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-04-21 15:05:29 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.059 |  |
| 2026-04-21 15:05:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-04-21 15:04:46 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:04:37 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.127 |  |
| 2026-04-21 15:04:33 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-21 15:04:26 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 15:09:38 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-04-21 15:06:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-21 15:07:23 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-21 15:03:51 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-21 15:01:49 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 15:01:14 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-21 15:03:12 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 15:03:21 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 15:12:44 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:01:45 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:15:41 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:06:36 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:15:56 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:17:07 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:03:17 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:04:46 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-21 15:06:36 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-21 15:02:14 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-04-21 15:04:33 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-21 15:01:48 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-21 15:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-21 15:02:39 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.012 |  |
| 2026-04-21 14:15:49 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-04-21 15:03:20 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | -0.019 |  |
| 2026-04-21 15:07:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-21 15:05:59 | Galgamuwa (Mee Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-04-21 15:00:11 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-21 15:05:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-04-21 15:00:24 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.030 |  |
| 2026-04-21 15:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.030 |  |
| 2026-04-21 15:02:10 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.036 |  |
| 2026-04-21 15:01:19 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.042 |  |
| 2026-04-21 15:03:16 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.044 |  |
| 2026-04-21 15:03:13 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2026-04-21 15:01:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.051 |  |
| 2026-04-21 15:05:29 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.059 |  |
| 2026-04-21 15:01:22 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.064 |  |
| 2026-04-21 15:04:26 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.066 |  |
| 2026-04-21 15:04:37 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)