# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_13:06:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,847 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 13:06:06 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-05 13:05:41 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:49 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:07 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:03 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.074 |  |
| 2026-04-05 13:03:51 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.013 |  |
| 2026-04-05 13:03:48 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:03:43 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:03:27 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:03:24 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-05 13:03:17 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-05 13:03:11 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:03:08 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.253 |  |
| 2026-04-05 13:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-05 13:02:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:37 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 13:02:26 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:22 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:07 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:50 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:38 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:36 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:36 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:01:31 | Thanthirimale (Malwathu Oya) | 2.88 | 🟢 Normal | -0.060 |  |
| 2026-04-05 13:01:13 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.148 |  |
| 2026-04-05 13:00:56 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.033 |  |
| 2026-04-05 12:18:41 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 13:03:24 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-05 13:06:06 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-05 12:09:23 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-05 13:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-05 13:02:37 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 13:02:22 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:50 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-05 12:01:41 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:36 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:07 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:05:41 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-05 12:10:31 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:03:27 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:38 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-04-05 12:03:35 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:26 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 12:00:56 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 12:06:19 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:49 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 12:09:28 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:03:43 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:07 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 12:03:31 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-04-05 12:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-04-05 13:03:17 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-05 12:02:48 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-04-05 13:03:51 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.013 |  |
| 2026-04-05 13:03:48 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:03:11 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:01:36 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-04-05 12:05:34 | Baddegama (Gin Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-04-05 13:00:56 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.033 |  |
| 2026-04-05 12:06:46 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.038 |  |
| 2026-04-05 13:01:31 | Thanthirimale (Malwathu Oya) | 2.88 | 🟢 Normal | -0.060 |  |
| 2026-04-05 13:04:03 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.074 |  |
| 2026-04-05 13:01:13 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.148 |  |
| 2026-04-05 13:03:08 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)