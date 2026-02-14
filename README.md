# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_09:21:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,704 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 09:21:32 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:10:14 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:09:56 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.014 |  |
| 2026-02-14 09:09:23 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 09:07:32 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:07:03 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:06:33 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-02-14 09:06:19 | Dunamale (Aththanagalu Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-14 09:06:09 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.189 |  |
| 2026-02-14 09:05:44 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:05:41 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:05:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-02-14 09:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.075 |  |
| 2026-02-14 09:04:38 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2026-02-14 09:04:12 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.049 |  |
| 2026-02-14 09:04:10 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-14 09:04:02 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:03:43 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:03:11 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 09:03:08 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:03:05 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:03:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:58 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-14 09:02:37 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-02-14 09:02:23 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.021 |  |
| 2026-02-14 09:02:20 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:16 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-14 09:02:10 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:08 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:04 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:02 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:01:49 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 09:01:43 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-02-14 09:01:33 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-14 09:01:14 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.030 |  |
| 2026-02-14 09:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:00:59 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:00:38 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 09:00:09 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 09:04:10 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-14 09:02:58 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-14 09:03:11 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 09:01:49 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 09:00:38 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 09:09:23 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 09:07:32 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:20 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:04 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:21:32 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:08 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:05:44 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:10 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:04:02 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:03:05 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:00:59 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:03:08 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:02:37 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:07:03 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:03:43 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:03:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:10:14 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 09:05:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-02-14 08:08:11 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-02-14 09:06:19 | Dunamale (Aththanagalu Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-14 09:02:16 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-14 09:01:33 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-14 09:00:09 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.011 |  |
| 2026-02-14 09:01:43 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-02-14 09:09:56 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.014 |  |
| 2026-02-14 09:06:33 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-02-14 09:02:23 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.021 |  |
| 2026-02-14 09:04:38 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2026-02-14 09:01:14 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.030 |  |
| 2026-02-14 09:02:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-02-14 09:04:12 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.049 |  |
| 2026-02-14 09:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.075 |  |
| 2026-02-14 09:06:09 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)