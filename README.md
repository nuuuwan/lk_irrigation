# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_14:19:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,945 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 14:19:23 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-02-23 14:11:09 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.027 |  |
| 2026-02-23 14:11:07 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 14:10:34 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.029 |  |
| 2026-02-23 14:10:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2026-02-23 14:09:06 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.056 |  |
| 2026-02-23 14:08:45 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:08:20 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-23 14:08:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-02-23 14:06:15 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-02-23 14:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.096 |  |
| 2026-02-23 14:05:44 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:05:14 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 14:05:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-23 14:04:59 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-02-23 14:04:13 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:03:27 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-02-23 14:03:12 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:03:11 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:03:11 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-02-23 14:03:09 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.024 |  |
| 2026-02-23 14:02:52 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.101 |  |
| 2026-02-23 14:02:33 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:21 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.099 |  |
| 2026-02-23 14:02:17 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:16 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:12 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 14:02:10 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:08 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:02 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:01:53 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:01:48 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:01:25 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:00:40 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-23 14:00:40 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-02-23 14:00:33 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 14:05:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-23 14:00:40 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-23 14:08:20 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-23 14:11:07 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 14:05:14 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 14:02:12 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 14:06:15 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-02-23 14:08:45 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:17 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:08 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:03:11 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:01:48 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:16 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:04:13 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:02 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:03:12 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:00:33 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:01:53 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:02:10 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-02-23 14:00:40 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-02-23 14:04:59 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-02-23 14:10:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2026-02-23 14:19:23 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-02-23 14:03:11 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-02-23 14:02:33 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:05:44 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:01:25 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-02-23 14:03:09 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.024 |  |
| 2026-02-23 14:11:09 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.027 |  |
| 2026-02-23 14:08:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-02-23 14:10:34 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.029 |  |
| 2026-02-23 14:03:27 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-02-23 13:07:07 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.052 |  |
| 2026-02-23 14:09:06 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.056 |  |
| 2026-02-23 13:02:06 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.061 |  |
| 2026-02-23 14:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.096 |  |
| 2026-02-23 14:02:21 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | -0.099 |  |
| 2026-02-23 14:02:52 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)