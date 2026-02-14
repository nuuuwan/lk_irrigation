# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_10:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,742 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 10:14:58 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:12:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-14 10:09:34 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 10:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.037 |  |
| 2026-02-14 10:08:02 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:07:18 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-02-14 10:07:10 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 10:06:25 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:05:00 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 10:04:33 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-02-14 10:04:25 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:04:24 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:04:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.005 |  |
| 2026-02-14 10:04:08 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:04:02 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 10:03:59 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-02-14 10:03:54 | Dunamale (Aththanagalu Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:03:48 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.224 |  |
| 2026-02-14 10:03:38 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.021 |  |
| 2026-02-14 10:03:31 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.042 |  |
| 2026-02-14 10:03:24 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-02-14 10:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:56 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:46 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-14 10:02:29 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:27 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:27 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-14 10:02:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:01 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-14 10:01:58 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-02-14 10:01:33 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:01:29 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:01:16 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:00:59 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:00:51 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:00:45 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.022 |  |
| 2026-02-14 10:00:44 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:00:07 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 10:07:18 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-02-14 10:12:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-14 10:05:00 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 10:02:01 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-14 10:04:02 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 10:07:10 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 10:09:34 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-14 10:01:29 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:27 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:00:07 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:00:51 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:29 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:08:02 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:01:33 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:14:58 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:56 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:02:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:03:54 | Dunamale (Aththanagalu Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:00:44 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:04:25 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:04:24 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:06:25 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:04:08 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:00:59 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:01:16 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-14 10:04:12 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.005 |  |
| 2026-02-14 10:04:33 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-02-14 10:01:58 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-02-14 10:02:27 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-14 10:02:46 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-14 09:09:56 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.014 |  |
| 2026-02-14 10:03:24 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.020 |  |
| 2026-02-14 10:03:38 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.021 |  |
| 2026-02-14 10:00:45 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.022 |  |
| 2026-02-14 10:03:59 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-02-14 10:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.037 |  |
| 2026-02-14 10:03:31 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.042 |  |
| 2026-02-14 10:03:48 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)