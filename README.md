# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_04:07:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,547 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 04:07:52 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 04:07:11 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-23 04:06:49 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-02-23 04:06:16 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-23 04:06:02 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:06:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-23 04:05:26 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.094 |  |
| 2026-02-23 04:05:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -1.057 |  |
| 2026-02-23 04:05:16 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-02-23 04:04:52 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-23 04:04:23 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-23 04:03:56 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-02-23 04:03:50 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-02-23 04:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:03:33 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-02-23 04:02:49 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-02-23 04:02:39 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:55 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:51 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:49 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | -0.392 |  |
| 2026-02-23 04:01:35 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.169 |  |
| 2026-02-23 04:01:33 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:22 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:10 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.033 |  |
| 2026-02-23 04:01:05 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:00:43 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-23 04:00:33 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-02-23 03:17:20 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 04:02:49 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-02-23 04:06:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 04:00:43 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-23 03:06:01 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 04:01:22 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:02:39 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:12:42 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:55 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:06:02 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:51 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:05 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:04:49 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:09:24 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:33 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:06:49 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-02-23 04:04:52 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-23 04:07:11 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-23 04:07:52 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 04:06:16 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-02-23 03:04:00 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.015 |  |
| 2026-02-23 03:05:48 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-02-23 04:04:23 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-23 04:05:16 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-02-23 04:03:56 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-02-23 04:03:50 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-02-23 04:01:10 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.033 |  |
| 2026-02-23 04:00:33 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-02-23 04:03:33 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-02-23 03:17:20 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.062 |  |
| 2026-02-23 04:05:26 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.094 |  |
| 2026-02-23 03:08:40 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.106 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-23 04:01:35 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.169 |  |
| 2026-02-23 04:01:49 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | -0.392 |  |
| 2026-02-23 03:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | -1.029 |  |
| 2026-02-23 04:05:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -1.057 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)