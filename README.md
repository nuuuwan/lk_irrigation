# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_10:23:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 10:23:59 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.007 |  |
| 2026-04-14 10:23:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.076 |  |
| 2026-04-14 10:22:57 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.008 |  |
| 2026-04-14 10:20:46 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.016 |  |
| 2026-04-14 10:15:35 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.028 |  |
| 2026-04-14 10:14:22 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.017 |  |
| 2026-04-14 10:09:50 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -2.108 |  |
| 2026-04-14 10:09:17 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:07:56 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:07:54 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-04-14 10:07:28 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:07:21 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-14 10:07:21 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-04-14 10:06:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:05:48 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:04:54 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-04-14 10:04:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:04:46 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.082 |  |
| 2026-04-14 10:04:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 10:04:27 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-04-14 10:04:13 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-04-14 10:04:07 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:04:05 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:03:49 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.039 |  |
| 2026-04-14 10:03:23 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:03:16 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:03:12 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.058 |  |
| 2026-04-14 10:02:26 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:02:13 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.092 |  |
| 2026-04-14 10:02:02 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-14 10:01:40 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 10:01:40 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:01:31 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 10:01:14 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-04-14 10:01:04 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-04-14 10:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:00:45 | Kithulgala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.058 |  |
| 2026-04-14 10:00:31 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:00:24 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 10:01:31 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 10:04:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 10:01:40 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 10:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:06:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:07:56 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:03:23 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:07:28 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:02:26 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:05:48 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:04:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:03:16 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-14 10:23:59 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.007 |  |
| 2026-04-14 10:22:57 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.008 |  |
| 2026-04-14 10:07:21 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.009 |  |
| 2026-04-14 10:07:54 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-04-14 10:09:17 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:04:07 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:04:05 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:01:40 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:00:31 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:07:21 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-14 10:20:46 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.016 |  |
| 2026-04-14 10:14:22 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.017 |  |
| 2026-04-14 10:04:54 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-04-14 10:04:13 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-04-14 10:02:02 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-14 10:01:04 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-04-14 10:15:35 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.028 |  |
| 2026-04-14 10:04:27 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-04-14 10:00:24 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.030 |  |
| 2026-04-14 10:03:49 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.039 |  |
| 2026-04-14 10:01:14 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-04-14 10:00:45 | Kithulgala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.058 |  |
| 2026-04-14 10:03:12 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.058 |  |
| 2026-04-14 10:23:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.076 |  |
| 2026-04-14 10:04:46 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.082 |  |
| 2026-04-14 10:02:13 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.092 |  |
| 2026-04-14 10:09:50 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -2.108 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)