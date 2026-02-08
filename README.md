# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_07:22:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 07:22:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:17:02 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-02-08 07:14:26 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.008 |  |
| 2026-02-08 07:11:24 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.017 |  |
| 2026-02-08 07:10:41 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.051 |  |
| 2026-02-08 07:09:09 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 07:08:35 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-02-08 07:08:01 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:08:01 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 07:07:45 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-02-08 07:06:24 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:05:40 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-08 07:05:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.120 |  |
| 2026-02-08 07:05:17 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:05:10 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-02-08 07:04:35 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:03:41 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:03:35 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-08 07:03:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:03:02 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.042 |  |
| 2026-02-08 07:02:55 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-02-08 07:02:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:02:31 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.005 |  |
| 2026-02-08 07:02:20 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-02-08 07:02:14 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:02:02 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-08 07:02:00 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:01:55 | Weraganthota (Mahaweli Ganga) | -2.13 | 🟢 Normal | -0.070 |  |
| 2026-02-08 07:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:01:33 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-02-08 07:01:24 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.022 |  |
| 2026-02-08 07:01:16 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.112 |  |
| 2026-02-08 07:00:47 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.014 |  |
| 2026-02-08 07:00:29 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 06:33:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.002 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 07:05:40 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-08 07:09:09 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 07:00:29 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 07:08:01 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 06:33:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.002 |  |
| 2026-02-08 07:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:02:43 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:09:22 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:05:17 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:03:41 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:06:24 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:02:14 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:03:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 06:07:43 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:08:01 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:02:00 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:04:35 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:22:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-08 07:02:31 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.005 |  |
| 2026-02-08 07:17:02 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-02-08 07:14:26 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.008 |  |
| 2026-02-08 06:15:33 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.008 |  |
| 2026-02-08 07:07:45 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-02-08 07:03:35 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-08 07:02:55 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-02-08 07:00:47 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.014 |  |
| 2026-02-08 07:11:24 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.017 |  |
| 2026-02-08 07:05:10 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-02-08 07:08:35 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-02-08 07:01:24 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | -0.022 |  |
| 2026-02-08 07:02:20 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-02-08 07:02:02 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-08 07:03:02 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.042 |  |
| 2026-02-08 07:10:41 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.051 |  |
| 2026-02-08 07:01:33 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-02-08 07:01:55 | Weraganthota (Mahaweli Ganga) | -2.13 | 🟢 Normal | -0.070 |  |
| 2026-02-08 07:01:16 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.112 |  |
| 2026-02-08 07:05:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.120 |  |
| 2026-02-08 06:18:07 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)