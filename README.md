# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_18:16:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,580 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 18:16:12 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-02-09 18:09:57 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-02-09 18:09:52 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-02-09 18:09:00 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-09 18:07:49 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 18:06:49 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:06:11 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:05:45 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:05:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:05:00 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:04:41 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | -0.022 |  |
| 2026-02-09 18:04:34 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-09 18:04:30 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-09 18:04:04 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:03:59 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:03:43 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-09 18:03:20 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-02-09 18:02:51 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 18:02:51 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:02:50 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:48 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:47 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:32 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:31 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-02-09 18:02:09 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-02-09 18:01:51 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.080 |  |
| 2026-02-09 18:01:33 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:01:29 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-09 18:01:17 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:01:12 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-02-09 18:01:10 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:00:47 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:47 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-02-09 18:00:39 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-02-09 18:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -36.000 |  |
| 2026-02-09 18:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -36.000 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:06 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 18:00:47 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-02-09 18:04:30 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-09 18:02:51 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 18:02:47 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-09 18:03:43 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-09 18:04:34 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-09 18:01:29 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-09 18:07:49 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 18:00:06 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:01:10 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:03:59 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:31 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:06:11 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:05:00 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:48 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:50 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:01:17 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:01:33 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:05:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:32 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:06:49 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:04:04 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:09:52 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-02-09 18:09:00 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-02-09 18:09:57 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-02-09 18:05:45 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:47 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:02:51 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:01:12 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-02-09 18:02:09 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-02-09 18:16:12 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-02-09 18:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-02-09 18:04:41 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | -0.022 |  |
| 2026-02-09 18:03:20 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-02-09 18:00:39 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-02-09 18:01:51 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.080 |  |
| 2026-02-09 18:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)