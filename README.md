# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_13:15:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 13:15:41 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-02-23 13:13:48 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:10:00 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-02-23 13:09:17 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.036 |  |
| 2026-02-23 13:08:41 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-02-23 13:07:07 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.052 |  |
| 2026-02-23 13:06:15 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:05:46 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-02-23 13:05:14 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.039 |  |
| 2026-02-23 13:04:36 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:04:10 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-02-23 13:04:03 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-02-23 13:03:53 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-02-23 13:03:38 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-02-23 13:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.099 |  |
| 2026-02-23 13:03:18 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-02-23 13:02:43 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-02-23 13:02:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-23 13:02:18 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.032 |  |
| 2026-02-23 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:02:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:02:07 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:02:06 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.061 |  |
| 2026-02-23 13:02:04 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:58 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:57 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-02-23 13:01:51 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.054 |  |
| 2026-02-23 13:01:50 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:41 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:31 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.118 |  |
| 2026-02-23 13:01:19 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.175 |  |
| 2026-02-23 13:01:15 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:12 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.033 |  |
| 2026-02-23 13:01:07 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-02-23 13:00:48 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 13:00:44 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:00:40 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-23 13:00:00 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 12:03:48 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-23 13:00:48 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 13:02:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:58 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:15 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:13:48 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:02:04 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:04:36 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:41 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:00:44 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:06:15 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:01:50 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:02:07 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 13:10:00 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-02-23 13:15:41 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-02-23 13:04:10 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-02-23 13:02:43 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-02-23 13:02:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-23 13:00:40 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-23 13:00:00 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-02-23 13:01:57 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-02-23 13:03:53 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.019 |  |
| 2026-02-23 13:08:41 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-02-23 13:03:18 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-02-23 13:03:38 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-02-23 13:01:07 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-02-23 13:05:46 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-02-23 13:04:03 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-02-23 13:02:18 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.032 |  |
| 2026-02-23 13:01:12 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.033 |  |
| 2026-02-23 13:09:17 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.036 |  |
| 2026-02-23 13:05:14 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.039 |  |
| 2026-02-23 13:07:07 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.052 |  |
| 2026-02-23 13:01:51 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.054 |  |
| 2026-02-23 13:02:06 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.061 |  |
| 2026-02-23 13:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.099 |  |
| 2026-02-23 13:01:31 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.118 |  |
| 2026-02-23 13:01:19 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)