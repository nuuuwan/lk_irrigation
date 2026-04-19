# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_09:30:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,153 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 09:30:24 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:12:37 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:11:57 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 09:11:54 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.018 |  |
| 2026-04-19 09:09:31 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:08:47 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.049 |  |
| 2026-04-19 09:08:30 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-04-19 09:08:05 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.084 |  |
| 2026-04-19 09:07:55 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:07:07 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:06:12 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:05:13 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-04-19 09:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.052 |  |
| 2026-04-19 09:05:10 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:05:00 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:04:58 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:04:41 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 1.540 | 🔺 Rising |
| 2026-04-19 09:04:25 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-19 09:04:25 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:03:07 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-04-19 09:03:07 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:03:01 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.293 |  |
| 2026-04-19 09:02:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:02:20 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.050 |  |
| 2026-04-19 09:02:12 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-19 09:02:07 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:53 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.085 |  |
| 2026-04-19 09:01:47 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:42 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:26 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:26 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:15 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-04-19 09:01:14 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.021 |  |
| 2026-04-19 09:01:14 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:01 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-19 09:00:54 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:00:24 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-19 09:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-19 09:00:14 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 09:04:41 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 1.540 | 🔺 Rising |
| 2026-04-19 09:02:12 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-19 09:04:25 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-19 09:00:24 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-19 09:01:01 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-19 09:11:57 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 09:00:54 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:26 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:04:25 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:02:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:03:07 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:30:24 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:07:55 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:47 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:04:58 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:26 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:12:37 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:07:07 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:06:12 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:05:00 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:05:10 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:09:31 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:01:14 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:02:07 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-19 09:08:30 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-04-19 09:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-19 09:01:15 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-04-19 09:11:54 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.018 |  |
| 2026-04-19 09:03:07 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-04-19 09:01:14 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.021 |  |
| 2026-04-19 09:00:14 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-04-19 09:05:13 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-04-19 09:08:47 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.049 |  |
| 2026-04-19 09:02:20 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.050 |  |
| 2026-04-19 09:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.052 |  |
| 2026-04-19 09:08:05 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.084 |  |
| 2026-04-19 09:01:53 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.085 |  |
| 2026-04-19 06:01:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.086 |  |
| 2026-04-19 09:03:01 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.293 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)