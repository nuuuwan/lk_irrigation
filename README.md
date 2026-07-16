# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_13:03:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **207,783 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 13:03:10 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-07-16 13:03:03 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:02:58 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:02:55 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-16 13:02:53 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-16 13:02:43 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:02:31 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.021 |  |
| 2026-07-16 13:02:22 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:02:17 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-07-16 13:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-16 13:01:29 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 13:01:11 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:00:49 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:00:26 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.010 |  |
| 2026-07-16 12:14:49 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 13:02:17 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-07-16 12:06:12 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-16 12:02:21 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-16 13:02:53 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-16 12:04:02 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-16 13:01:29 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 12:03:10 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:00:49 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:01:09 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:02:00 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:02:59 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:02:22 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:04:32 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:01:24 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:00:24 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:02:58 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:02:43 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:07:23 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:02:04 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:03:03 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:03:57 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:05:35 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:14:49 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:08:31 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:02:54 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:01:36 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-16 13:01:11 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:00:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-07-16 12:05:46 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-07-16 13:02:55 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-16 13:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-16 13:00:26 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.010 |  |
| 2026-07-16 13:03:10 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-07-16 13:02:31 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.021 |  |
| 2026-07-16 12:01:07 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-07-16 12:03:17 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | -0.023 |  |
| 2026-07-16 12:07:48 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-07-16 12:01:13 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.070 |  |
| 2026-07-16 12:03:37 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)