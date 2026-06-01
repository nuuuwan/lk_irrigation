# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_09:14:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,371 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 09:14:11 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.831 | 🔺 Rising |
| 2026-06-01 09:09:27 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:08:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.019 |  |
| 2026-06-01 09:07:38 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:07:37 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-01 09:06:46 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:06:33 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:06:11 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.214 |  |
| 2026-06-01 09:05:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:05:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.067 |  |
| 2026-06-01 09:05:09 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:04:46 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-06-01 09:04:15 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | -0.021 |  |
| 2026-06-01 09:03:52 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:03:51 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:03:46 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-06-01 09:03:43 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 09:03:43 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-01 09:03:25 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.093 |  |
| 2026-06-01 09:03:23 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:03:14 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.011 |  |
| 2026-06-01 09:03:13 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:02:55 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.049 |  |
| 2026-06-01 09:02:55 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.020 |  |
| 2026-06-01 09:02:44 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.021 |  |
| 2026-06-01 09:02:31 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:02:31 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-06-01 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.020 |  |
| 2026-06-01 09:02:17 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:02:06 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:01:37 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-06-01 09:01:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 09:01:34 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:01:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 09:01:27 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:00:47 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-06-01 09:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 09:14:11 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.831 | 🔺 Rising |
| 2026-06-01 09:03:43 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 09:01:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 09:01:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 09:06:46 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:01:34 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:02:06 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:06:33 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:03:52 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:03:13 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:03:51 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:05:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:09:27 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:02:31 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 08:04:57 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:02:17 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:01:27 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:05:09 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:03:23 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:07:38 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 09:03:46 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-06-01 09:07:37 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-01 09:03:43 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-01 09:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-01 09:04:46 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-06-01 09:01:37 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-06-01 09:03:14 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.011 |  |
| 2026-06-01 09:08:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.019 |  |
| 2026-06-01 09:02:55 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.020 |  |
| 2026-06-01 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.020 |  |
| 2026-06-01 09:04:15 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | -0.021 |  |
| 2026-06-01 09:02:44 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.021 |  |
| 2026-06-01 09:02:31 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-06-01 09:00:47 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-06-01 09:02:55 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.049 |  |
| 2026-06-01 09:05:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.067 |  |
| 2026-06-01 09:03:25 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.093 |  |
| 2026-06-01 08:05:59 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.104 |  |
| 2026-06-01 09:06:11 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)