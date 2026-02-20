# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_08:05:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,980 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 08:05:48 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-20 08:04:49 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-20 08:04:44 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:04:29 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.011 |  |
| 2026-02-20 08:03:45 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 08:03:41 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 08:03:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-02-20 08:03:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:03:27 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.157 |  |
| 2026-02-20 08:02:59 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:54 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-20 08:02:47 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.180 |  |
| 2026-02-20 08:02:36 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-02-20 08:02:17 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:14 | Weraganthota (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:05 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:00 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-20 08:01:52 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 08:01:34 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:01:22 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:01:21 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:01:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:00:12 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-20 08:00:07 | Padiyathalawa (Maduru Oya) | 4.10 | 🟡 Alert | 0.188 | 🔺 Rising |
| 2026-02-20 07:24:31 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:21:44 | Padiyathalawa (Maduru Oya) | 3.98 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-02-20 07:16:47 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:11:53 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:11:47 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 08:00:07 | Padiyathalawa (Maduru Oya) | 4.10 | 🟡 Alert | 0.188 | 🔺 Rising |
| 2026-02-20 07:06:30 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-20 08:04:49 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-20 06:05:09 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 08:05:48 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-20 08:00:12 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-20 08:01:52 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 08:03:41 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 08:03:45 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 08:01:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:14 | Weraganthota (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:01:21 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:01:22 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:00:25 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:09:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:36 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:05 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:05:24 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:11:47 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:01:00 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:59 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:17 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:04:44 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:03:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:24:31 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 07:10:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:01:34 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 08:02:54 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-20 08:02:00 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-20 08:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-02-20 08:04:29 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.011 |  |
| 2026-02-20 07:04:52 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.020 |  |
| 2026-02-20 08:03:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-02-20 07:05:05 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.056 |  |
| 2026-02-20 08:03:27 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.157 |  |
| 2026-02-20 08:02:47 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.180 |  |
| 2026-02-20 07:06:11 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -138.150 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)