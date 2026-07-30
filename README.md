# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_21:23:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,624 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 21:23:23 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:12:03 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:10:40 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-30 21:10:40 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:07:41 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-07-30 21:07:02 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:06:22 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-30 21:05:51 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.030 |  |
| 2026-07-30 21:05:49 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:05:48 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-07-30 21:04:51 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-07-30 21:04:17 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:04:10 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:57 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:51 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:30 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:29 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:26 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-07-30 21:03:14 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:02 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:59 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:44 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:40 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-30 21:02:39 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-07-30 21:02:34 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:34 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:23 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.289 |  |
| 2026-07-30 21:02:14 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-07-30 21:02:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:01:26 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-07-30 21:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:01:01 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-30 21:00:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.125 |  |
| 2026-07-30 20:59:49 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 21:04:51 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-07-30 21:01:01 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-30 21:02:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:59 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:51 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 20:01:58 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:30 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:23:23 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:29 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:05:49 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:34 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:10:40 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:05:48 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:12:03 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:34 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:14 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:02 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 20:59:49 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:04:17 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:57 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:04:10 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:07:02 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:02:44 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 21:03:26 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-07-30 21:10:40 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:01:03 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-30 21:02:40 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-30 21:02:39 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-07-30 21:07:41 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-07-30 21:06:22 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-30 21:02:14 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-07-30 21:05:51 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.030 |  |
| 2026-07-30 21:01:26 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-07-30 21:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.051 |  |
| 2026-07-30 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.060 |  |
| 2026-07-30 21:00:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.125 |  |
| 2026-07-30 21:02:23 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.289 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)