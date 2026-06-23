# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_02:15:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,674 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 02:15:47 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.008 |  |
| 2026-06-24 02:12:25 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.76 | 🟡 Alert | -0.065 |  |
| 2026-06-24 02:10:51 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:10:45 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:09:09 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.052 |  |
| 2026-06-24 02:08:34 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:07:20 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-24 02:06:43 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-06-24 02:06:36 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:06:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-06-24 02:05:42 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.030 |  |
| 2026-06-24 02:05:06 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:04:28 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.048 |  |
| 2026-06-24 02:04:16 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.049 |  |
| 2026-06-24 02:03:57 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-06-24 02:03:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:03:44 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-06-24 02:03:43 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:03:18 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.061 |  |
| 2026-06-24 02:03:14 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:03:12 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-06-24 02:02:28 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | -0.070 |  |
| 2026-06-24 02:02:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:01:53 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.012 |  |
| 2026-06-24 02:01:28 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:01:22 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-06-24 02:01:08 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:01:04 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:00:42 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.226 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 02:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.76 | 🟡 Alert | -0.065 |  |
| 2026-06-24 02:02:28 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | -0.070 |  |
| 2026-06-24 01:06:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-24 02:01:28 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:01:04 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:01:08 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:10:51 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:10:45 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:03:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:03:14 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:03:43 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:06:14 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:05:06 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:06:36 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:02:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:12:25 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 02:15:47 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.008 |  |
| 2026-06-24 02:07:20 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-24 02:01:22 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-06-24 02:03:44 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 02:03:57 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-06-24 02:01:53 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.012 |  |
| 2026-06-24 00:11:59 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-06-24 02:03:12 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-06-24 02:05:42 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.030 |  |
| 2026-06-24 02:06:43 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-06-24 01:02:59 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.031 |  |
| 2026-06-24 00:22:14 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.039 |  |
| 2026-06-24 02:04:28 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.048 |  |
| 2026-06-24 02:04:16 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.049 |  |
| 2026-06-24 02:09:09 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | -0.052 |  |
| 2026-06-24 01:00:37 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2026-06-24 02:06:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-06-24 02:03:18 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.061 |  |
| 2026-06-24 02:00:42 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.226 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)