# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_10:21:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,020 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 10:21:30 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-06-05 10:18:26 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-05 10:15:05 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-05 10:12:25 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-05 10:07:32 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-06-05 10:07:14 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-06-05 10:06:01 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 10:05:58 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:05:35 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 10:05:34 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.039 |  |
| 2026-06-05 10:05:33 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:05:31 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.070 |  |
| 2026-06-05 10:05:02 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:05:00 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | -0.016 |  |
| 2026-06-05 10:04:50 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:04:08 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.030 |  |
| 2026-06-05 10:04:04 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:03:57 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-05 10:03:50 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.039 |  |
| 2026-06-05 10:03:50 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.030 |  |
| 2026-06-05 10:03:49 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:03:47 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-05 10:03:45 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-06-05 10:03:43 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:03:32 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.040 |  |
| 2026-06-05 10:03:27 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:03:25 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:03:16 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-05 10:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:02:47 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:02:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:02:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-05 10:02:02 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 10:01:52 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-05 10:01:45 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-06-05 10:01:28 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:00:37 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 10:12:25 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-05 10:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-05 10:03:57 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-05 10:15:05 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-05 10:03:16 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-05 10:05:35 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 09:06:13 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 10:03:47 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-05 10:06:01 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 10:02:02 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 10:18:26 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-05 10:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:05:02 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:02:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:02:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:05:58 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:03:49 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:04:04 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:03:25 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:05:33 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:02:47 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:03:43 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 10:21:30 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-06-05 10:07:32 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-06-05 10:03:27 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:01:28 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:00:37 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:04:50 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-05 10:03:45 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-06-05 10:05:00 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | -0.016 |  |
| 2026-06-05 10:07:14 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-06-05 10:04:08 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.030 |  |
| 2026-06-05 10:03:50 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.030 |  |
| 2026-06-05 10:03:50 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.039 |  |
| 2026-06-05 10:05:34 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.039 |  |
| 2026-06-05 10:03:32 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.040 |  |
| 2026-06-05 10:01:45 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | -0.040 |  |
| 2026-06-05 10:05:31 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)