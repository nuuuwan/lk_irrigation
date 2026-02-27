# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_11:09:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,404 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 11:09:36 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:08:16 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.009 |  |
| 2026-02-27 11:08:14 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:07:38 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:07:05 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:07:00 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:05:43 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:05:21 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-27 11:05:08 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:04:26 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:04:06 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:04:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.033 |  |
| 2026-02-27 11:03:59 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 11:03:57 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:03:44 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.058 |  |
| 2026-02-27 11:03:25 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-27 11:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-02-27 11:03:04 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:55 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:37 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-02-27 11:02:37 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:31 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.013 |  |
| 2026-02-27 11:02:16 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:15 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.179 |  |
| 2026-02-27 11:02:13 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:49 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:01:48 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-27 11:01:25 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:18 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:18 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:17 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:01:11 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-27 11:00:39 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:00:32 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.060 |  |
| 2026-02-27 11:00:31 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 11:01:11 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-27 11:03:25 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-27 11:05:21 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-27 11:03:59 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-27 11:01:29 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-27 11:00:31 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-27 11:01:25 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:00:39 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:18 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:48 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:03:57 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:13 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:08:14 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:37 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:16 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:03:04 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:55 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:18 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:02:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:04:26 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-27 10:08:58 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:01:17 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:07:00 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:09:36 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-27 11:08:16 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.009 |  |
| 2026-02-27 11:05:43 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:07:05 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:04:06 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:01:49 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:05:08 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-27 11:02:31 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.013 |  |
| 2026-02-27 11:04:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.033 |  |
| 2026-02-27 11:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-02-27 11:02:37 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-02-27 11:03:44 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.058 |  |
| 2026-02-27 11:00:32 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.060 |  |
| 2026-02-27 11:02:15 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)