# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_19:31:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,146 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **48** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 19:31:04 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:24:07 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.007 |  |
| 2026-02-23 19:15:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.134 |  |
| 2026-02-23 19:13:50 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.005 |  |
| 2026-02-23 19:13:33 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:12:35 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.046 |  |
| 2026-02-23 19:10:31 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:09:35 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -18.000 |  |
| 2026-02-23 19:09:33 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -18.000 |  |
| 2026-02-23 19:09:32 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -18.000 |  |
| 2026-02-23 19:09:31 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -18.000 |  |
| 2026-02-23 19:09:30 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -18.000 |  |
| 2026-02-23 19:09:29 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -18.000 |  |
| 2026-02-23 19:09:13 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:09:12 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:09:11 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:09:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:09:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:07:41 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.046 |  |
| 2026-02-23 19:07:29 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:07:27 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:07:26 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:07:25 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:07:24 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-23 19:07:22 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:06:51 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-23 19:06:35 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-02-23 19:05:58 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:05:46 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:05:38 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.094 |  |
| 2026-02-23 19:05:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.060 |  |
| 2026-02-23 19:04:57 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-02-23 19:03:52 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 19:03:36 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:03:32 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 19:03:32 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:03:06 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:02:34 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:02:21 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-23 19:02:20 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-23 19:02:19 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:02:09 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.012 |  |
| 2026-02-23 19:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-02-23 19:01:43 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 19:01:36 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:01:10 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.059 |  |
| 2026-02-23 19:00:26 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:00:08 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 19:06:51 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-23 19:03:52 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 19:00:26 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:07:29 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:03:06 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:01:36 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:02:19 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:02:34 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:05:58 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:13:33 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:10:31 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:03:36 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:03:32 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:05:46 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:31:04 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:09:13 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-23 19:13:50 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.005 |  |
| 2026-02-23 19:24:07 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.007 |  |
| 2026-02-23 19:07:24 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-23 19:06:35 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-02-23 19:04:57 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-02-23 19:03:32 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 19:01:43 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 19:02:20 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-23 18:01:46 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-23 19:02:21 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-23 19:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-02-23 19:02:09 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.012 |  |
| 2026-02-23 19:00:08 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-23 19:12:35 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.046 |  |
| 2026-02-23 19:07:41 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.046 |  |
| 2026-02-23 19:01:10 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.059 |  |
| 2026-02-23 19:05:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.060 |  |
| 2026-02-23 19:05:38 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.094 |  |
| 2026-02-23 19:15:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.134 |  |
| 2026-02-23 19:09:35 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)