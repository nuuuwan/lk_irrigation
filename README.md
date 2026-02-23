# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_18:14:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 18:14:09 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-02-23 18:12:31 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.035 |  |
| 2026-02-23 18:11:53 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:10:05 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.070 |  |
| 2026-02-23 18:09:58 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.031 |  |
| 2026-02-23 18:06:43 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.039 |  |
| 2026-02-23 18:05:04 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:04:58 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:04:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:04:48 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:04:33 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-02-23 18:04:09 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.117 |  |
| 2026-02-23 18:03:57 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-23 18:03:11 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 18:03:08 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-02-23 18:03:06 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.041 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:40 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:20 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.039 |  |
| 2026-02-23 18:02:07 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.013 |  |
| 2026-02-23 18:01:58 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:01:53 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:01:48 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:01:46 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 18:04:33 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-02-23 18:01:35 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-23 18:01:32 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-23 18:03:11 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 18:01:58 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:04:09 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:05:04 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:01:13 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:04:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:40 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:03:57 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:14:09 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-02-23 18:04:48 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:11:53 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:01:48 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:01:46 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:04:58 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:01:05 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-23 17:09:20 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:01:20 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:01:48 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:01:43 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:01:36 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-02-23 18:02:07 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.013 |  |
| 2026-02-23 18:03:08 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:05:44 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-23 14:10:34 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.029 |  |
| 2026-02-23 18:01:41 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-02-23 18:09:58 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.031 |  |
| 2026-02-23 18:12:31 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.035 |  |
| 2026-02-23 18:06:43 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.039 |  |
| 2026-02-23 18:02:20 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.039 |  |
| 2026-02-23 18:03:06 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.041 |  |
| 2026-02-23 18:10:05 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.070 |  |
| 2026-02-23 18:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.117 |  |
| 2026-02-23 18:00:44 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.327 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)