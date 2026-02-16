# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_10:03:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 10:03:01 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 10:02:58 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.233 |  |
| 2026-02-16 10:02:54 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-02-16 10:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-02-16 10:02:19 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -1.103 |  |
| 2026-02-16 10:02:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:02:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-16 10:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:47 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.043 |  |
| 2026-02-16 10:01:45 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:01:29 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-02-16 10:01:25 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:23 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:13 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:09 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:08 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-02-16 10:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:01 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:00:46 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:00:39 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:57:41 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:57:15 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:18:33 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-02-16 09:08:14 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:07:53 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-16 09:07:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 09:18:33 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-02-16 09:07:53 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-16 09:04:14 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-16 10:03:01 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 10:02:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-16 10:01:09 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:00:57 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:02:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:23 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:01 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:03:17 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:18:19 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:13 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:00:39 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:01:25 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:07:19 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:05:35 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:04:50 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:04:07 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-16 09:01:11 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-16 10:00:46 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 08:04:23 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-02-16 09:06:41 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-02-16 09:02:46 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:01:45 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-16 10:01:08 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-02-16 09:05:24 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.014 |  |
| 2026-02-16 10:02:54 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-02-16 10:01:29 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-02-16 10:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-02-16 09:05:33 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.041 |  |
| 2026-02-16 10:01:47 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.043 |  |
| 2026-02-16 09:01:31 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.058 |  |
| 2026-02-16 09:04:11 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.059 |  |
| 2026-02-16 10:02:58 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.233 |  |
| 2026-02-16 10:02:19 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -1.103 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)