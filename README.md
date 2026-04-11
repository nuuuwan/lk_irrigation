# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_16:09:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 16:09:45 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-04-11 16:09:08 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:08:31 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:08:14 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:08:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-11 16:07:19 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-04-11 16:07:05 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:06:41 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-11 16:06:24 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:05:03 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:04:58 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-11 16:04:32 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:04:15 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:04:14 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:04:04 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:03:31 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.021 |  |
| 2026-04-11 16:03:26 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:03:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:03:06 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:02:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:02:53 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-11 16:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-11 16:02:27 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:02:22 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.030 |  |
| 2026-04-11 16:02:02 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:01:51 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:01:41 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-04-11 16:01:30 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.060 |  |
| 2026-04-11 16:01:06 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:01:02 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:00:42 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:00:38 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:00:35 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.040 |  |
| 2026-04-11 16:00:24 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 16:01:41 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-04-11 16:02:53 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-11 16:06:41 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-11 16:08:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-11 16:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-11 16:00:24 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 16:00:42 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:08:31 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:03:06 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:02:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:04:04 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:08:14 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:09:08 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:02:27 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:05:03 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:02:02 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:07:05 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:03:26 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:04:32 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:04:14 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:11:24 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:03:11 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:03:15 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:06:24 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-11 16:09:45 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-04-11 16:04:15 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:00:38 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:01:02 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:01:06 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:01:51 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-11 16:07:19 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-04-11 16:04:58 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-11 16:03:31 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.021 |  |
| 2026-04-11 15:06:43 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.028 |  |
| 2026-04-11 16:02:22 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.030 |  |
| 2026-04-11 16:00:35 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.040 |  |
| 2026-04-11 16:01:30 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.060 |  |
| 2026-04-11 15:01:01 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)