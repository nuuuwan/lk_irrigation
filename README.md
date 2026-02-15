# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_18:10:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,940 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 18:10:15 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:09:45 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-15 18:08:13 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:08:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:06:38 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:05:12 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-02-15 18:05:10 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:05:04 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:05:01 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.057 |  |
| 2026-02-15 18:04:45 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:04:33 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:04:25 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-02-15 18:03:42 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:03:30 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-02-15 18:03:02 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:53 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:34 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-15 18:02:19 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-02-15 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:06 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:04 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:03 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:49 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-15 18:01:43 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-02-15 18:01:26 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:19 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.113 |  |
| 2026-02-15 18:01:18 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.052 |  |
| 2026-02-15 18:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:13 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:00:40 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.100 |  |
| 2026-02-15 18:00:32 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-15 18:00:28 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.036 |  |
| 2026-02-15 18:00:16 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |
| 2026-02-15 18:00:08 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:59:42 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:59:07 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:59:04 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 18:01:49 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-15 18:02:34 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-15 18:00:32 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-15 18:09:45 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-15 18:03:02 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:00:08 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:43 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:59:07 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:04 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:13 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:06 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:08:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:10:15 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:04:33 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-15 17:59:42 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:05:04 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:26 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:04:45 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:06:38 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:08:13 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:03:42 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:02:53 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:05:10 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:03:30 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-02-15 18:05:12 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-02-15 18:04:25 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-02-15 18:02:19 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-02-15 18:00:28 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.036 |  |
| 2026-02-15 17:03:11 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.043 |  |
| 2026-02-15 18:01:18 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | -0.052 |  |
| 2026-02-15 18:05:01 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.057 |  |
| 2026-02-15 18:01:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-02-15 18:00:16 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |
| 2026-02-15 18:00:40 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.100 |  |
| 2026-02-15 18:01:19 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)