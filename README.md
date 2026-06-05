# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_12:11:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 12:11:08 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -4.324 |  |
| 2026-06-05 12:09:21 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.031 |  |
| 2026-06-05 12:09:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:07:09 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.019 |  |
| 2026-06-05 12:06:31 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-05 12:06:25 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 12:06:06 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:05:55 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:05:30 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.082 |  |
| 2026-06-05 12:05:14 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-06-05 12:05:00 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 12:04:23 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-06-05 12:04:18 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-06-05 12:03:57 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:03:52 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-05 12:03:50 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:03:38 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-05 12:03:24 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 12:03:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:03:10 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.229 |  |
| 2026-06-05 12:02:58 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:45 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 12:02:39 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 12:02:12 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:09 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-05 12:01:50 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 12:01:29 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:01:22 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-06-05 12:01:15 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-05 12:01:15 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.034 |  |
| 2026-06-05 12:00:59 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-05 12:00:59 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:00:54 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:00:27 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:00:27 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -4.324 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 12:03:38 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-05 11:04:25 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-05 12:06:25 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 12:06:31 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-05 12:03:52 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-05 12:01:50 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 12:03:24 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 12:00:59 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-05 12:02:45 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 12:05:00 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 12:03:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:01:29 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:00:27 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:09 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:58 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:03:50 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:06:06 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:05:55 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:12 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:39 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:09:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:03:57 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:00:54 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:00:59 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:04:23 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-06-05 12:01:15 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-05 12:01:22 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-06-05 12:05:14 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-06-05 12:04:18 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-06-05 11:13:53 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-06-05 12:07:09 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.019 |  |
| 2026-06-05 12:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-05 12:09:21 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.031 |  |
| 2026-06-05 12:01:15 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.034 |  |
| 2026-06-05 12:05:30 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.082 |  |
| 2026-06-05 12:03:10 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.229 |  |
| 2026-06-05 12:11:08 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -4.324 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)