# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_18:11:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,515 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 18:11:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-30 18:10:15 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:07:59 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:07:02 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:06:37 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.029 |  |
| 2026-07-30 18:06:21 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.020 |  |
| 2026-07-30 18:06:18 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:05:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:05:30 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.081 |  |
| 2026-07-30 18:05:04 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:51 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.081 |  |
| 2026-07-30 18:04:37 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:04:30 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:11 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:03:56 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:03:55 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-30 18:03:48 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:03:05 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.050 |  |
| 2026-07-30 18:02:28 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:22 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:11 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:06 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:05 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:01:56 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:01:46 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-30 18:01:44 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.063 |  |
| 2026-07-30 18:01:35 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:01:24 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:01:09 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:01:09 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.034 |  |
| 2026-07-30 18:01:03 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:00:27 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-30 18:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-07-30 18:00:22 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.123 |  |
| 2026-07-30 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 18:03:55 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-30 18:11:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-30 17:17:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-30 18:01:46 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-30 18:00:27 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-30 18:03:48 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-30 17:00:18 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:01:35 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:30 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:06:18 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:05:04 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:05 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:28 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:07:59 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:05:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:10:15 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:22 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:11 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:07:02 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:01:24 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:03:05 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:03:56 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:06 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:02:11 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:01:03 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:04:37 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:01:56 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:01:09 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-07-30 18:06:21 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.020 |  |
| 2026-07-30 18:06:37 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.029 |  |
| 2026-07-30 18:01:09 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.034 |  |
| 2026-07-30 18:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.050 |  |
| 2026-07-30 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.060 |  |
| 2026-07-30 18:01:44 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.063 |  |
| 2026-07-30 18:04:51 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.081 |  |
| 2026-07-30 18:05:30 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.081 |  |
| 2026-07-30 18:00:22 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)